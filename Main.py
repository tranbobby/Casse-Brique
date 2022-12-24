import pygame
from Paddle import Paddle
from Window import Window
from Ball import Ball
from Brick import Brick

# Définition des couleurs (R, G, B)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# window height and width
objWindow = Window(600, 400)
# Paddle speed, width and height
objPaddle = Paddle(5, 75, 20)
# Ball speed and size
objBall = Ball(5, 20)
# Brick : space between them, height and width
objBrick = Brick(20, 50, 20)

# Création des briques
bricks = objBrick.createBrick()

# création de la raquette
paddle = objPaddle.createPaddle(objWindow)

# création de la fenêtre
window = objWindow.createWindow()

# création de la balle

ball = objBall.createBall(objWindow)

# Définition de la direction initiale de la balle
# (1, 1) correspond à un déplacement vers la droite et vers le haut
# (-1, 1) correspond à un déplacement vers la gauche et vers le haut
direction = (1, 1)


# Boucle principale
while True:
    # Gestion des événements
    for event in pygame.event.get():
        # Si l'utilisateur quitte, on arrête la boucle
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Déplacement de la raquette avec les flèches gauche et droite
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= objPaddle.getSpeed()
    if keys[pygame.K_RIGHT]:
        paddle.x += objPaddle.getSpeed()

    # Empêcher la raquette de sortir de l'écran
    if paddle.x < 0:
        paddle.x = 0
    if paddle.x > objWindow.getWidth() - objPaddle.getWidth():
        paddle.x = objWindow.getWidth() - objPaddle.getWidth()

    # Déplacement de la balle
    ball.x += direction[0] * objBall.getSpeed()
    ball.y += direction[1] * objBall.getSpeed()

    # Inversion de la direction de la balle si elle touche un bord de l'écran
    if ball.x > objWindow.getWidth() - objBall.getSize() or ball.x < 0:
        direction = (-direction[0], direction[1])
    if ball.y < 0:
        direction = (direction[0], -direction[1])

    # Si la balle touche la raquette, on inverse sa direction
    if ball.colliderect(paddle):
        direction = (direction[0], -direction[1])

    # Suppression de la brique si la balle la touche
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            direction = (direction[0], -direction[1])

    # Arrêt de la boucle si toutes les briques ont été détruites
    if len(bricks) == 0:
        break

    # Remplissage de l'écran en noir
    window.fill(black)

    # Dessin de la balle et de la raquette
    pygame.draw.rect(window, white, ball)
    pygame.draw.rect(window, white, paddle)

    # Dessin des briques
    for brick in bricks:
        pygame.draw.rect(window, red, brick)

    # Mise à jour de l'affichage
    pygame.display.update()

    # Limitation de la fréquence de rafraîchissement à 60 FPS
    pygame.time.Clock().tick(60)
