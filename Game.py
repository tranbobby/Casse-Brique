import pygame


class Game:

    def __init__(self, paddle, ball, bricks, fps, direction) -> None:
        self.paddle = paddle
        self.ball = ball
        self.bricks = bricks
        self.fps = fps
        self.direction = direction

    def setPaddle(self, pdl):
        self.paddle = pdl

    def setBall(self, bll):
        self.ball = bll

    def setBricks(self, brcks):
        self.bricks = brcks

    def setFps(self, f):
        self.brick = f

    def setDirection(self, drtion):
        self.direction = drtion

    def getPaddle(self):
        return self.paddle

    def getBall(self):
        return self.ball

    def getBricks(self):
        return self.bricks

    def getFps(self):
        return self.brick

    def getDirection(self):
        return self.direction

    def framePerSecond(self):
        # Limitation de la fréquence de rafraîchissement à 60 FPS
        pygame.time.Clock().tick(self.getFps())

    def playerQuit(self):
        # Gestion des événements
        for event in pygame.event.get():
            # Si l'utilisateur quitte, on arrête la boucle
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def paddleMove(self, objPaddle):
        # Déplacement de la raquette avec les flèches gauche et droite
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.x -= objPaddle.getSpeed()
        if keys[pygame.K_RIGHT]:
            self.paddle.x += objPaddle.getSpeed()

    def gameBorder(self, objWindow, objPaddle):
        # Empêcher la raquette de sortir de l'écran
        if self.getPaddle().x < 0:
            self.getPaddle().x = 0
        if self.getPaddle().x > objWindow.getWidth() - objPaddle.getWidth():
            self.getPaddle().x = objWindow.getWidth() - objPaddle.getWidth()

    def ballMove(self, objBall):
        # Déplacement de la balle
        self.getBall().x += self.getDirection()[0] * objBall.getSpeed()
        self.getBall().y += self.getDirection()[1] * objBall.getSpeed()

    def ballBounce(self, objWindow, objBall):
        # Inversion de la direction de la balle si elle touche un bord de l'écran
        if self.getBall().x > objWindow.getWidth() - objBall.getSize() or self.getBall().x < 0:
            self.setDirection(
                (-self.getDirection()[0], self.getDirection()[1]))
        if self.getBall().y < 0:
            self.setDirection((self.getDirection()[
                              0], -self.getDirection()[1]))

    def ballBounceDirection(self):
        # Si la balle touche la raquette, on inverse sa direction
        if self.getBall().colliderect(self.getPaddle()):
            self.setDirection(
                (self.getDirection()[0], -self.getDirection()[1]))

    def brickDelete(self):
        # Suppression de la brique si la balle la touche
        for brick in self.getBricks():
            if self.getBall().colliderect(brick):
                self.getBricks().remove(brick)
                self.setDirection((self.getDirection()[
                                  0], -self.getDirection()[1]))
