import pygame


class Brick:
    """
    Brick creation and settings class
    """

    def __init__(self, space, width, height):
        self.space = space
        self.width = width
        self.height = height

    def __str__(self):
        return "Brick : space :"+str(self.getSpace())+" width : "+str(self.getWidth())+" height : "+str(self.getHeight())

# setter

    def setSpace(self, space):
        self.space = space

    def setHeight(self, height):
        self.height = height

    def setWidth(self, width):
        self.width = width

# getter
    def getSpace(self):
        return self.space

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

# function
    def createBrick(self):
        bricks = []
        for i in range(5):
            for j in range(5):
                bricks.append(pygame.Rect(self.getSpace() + i * (self.getWidth() + self.getSpace()),
                                          self.getSpace() + j * (self.getHeight() + self.getSpace()), self.getWidth(), self.getHeight()))
        return bricks
