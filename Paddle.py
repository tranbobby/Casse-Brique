from Window import Window
import pygame


class Paddle:
    """
    Paddle settings and creation class
    """

    def __init__(self, speed, width, height):
        self.speed = speed
        self.width = width
        self.height = height

    def __str__(self):
        return "Paddle : speed :"+str(self.getSpeed())+" width : "+str(self.getWidth())+" height : "+str(self.getHeight())


# setter


    def setSpeed(self, speed):
        self.speed = speed

    def setHeight(self, height):
        self.height = height

    def setWidth(self, width):
        self.width = width

# getter
    def getSpeed(self):
        return self.speed

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

# function
    def createPaddle(self, window):
        return pygame.Rect(window.getWidth() // 2 - self.getWidth() // 2,
                           window.getHeight() - self.getHeight() - 10, self.getWidth(), self.getHeight())
