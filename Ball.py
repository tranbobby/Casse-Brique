import pygame


class Ball:
    """
    Ball creation and settings class
    """

    def __init__(self, speed, size):
        self.speed = speed
        self.size = size

    def __str__(self):
        return "Size : "

    # setter

    def setSpeed(self, speed):
        self.speed = speed

    def setSize(self, size):
        self.size = size


# getter


    def getSpeed(self):
        return self.speed

    def getSize(self):
        return self.size

# function

    def createBall(self, window):
        return pygame.Rect(window.getWidth() // 2, window.getHeight() //
                           2, self.getSize(), self.getSize())
