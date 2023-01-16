import pygame
from Paddle import Paddle
from Window import Window
from Ball import Ball
from Brick import Brick
from Game import Game

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

# création de l'objet jeu

objGame = Game(paddle, ball, bricks, 60, direction)


# Boucle principale
while True:

    objGame.playerQuit()

    objGame.paddleMove(objPaddle)

    # Empêcher la raquette de sortir de l'écran
    objGame.gameBorder(objWindow, objPaddle)

    # Déplacement de la balle
    objGame.ballMove(objBall)

    # Inversion de la direction de la balle si elle touche un bord de l'écran
    objGame.ballBounce(objWindow, objBall)

    # Si la balle touche la raquette, on inverse sa direction
    objGame.ballBounceDirection()

    # Suppression de la brique si la balle la touche
    objGame.brickDelete()

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
