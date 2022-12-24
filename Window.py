import pygame


class Window:
    """"
    Window Creation and setting class
    """

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return "Height : "+str(self.getHeight())+"Width : "+str(self.getWidth())

# setter
    def setHeight(self, height):
        self.height = height

    def setWidth(self, width):
        self.width = width

# getter
    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

# function
    def createWindow(self):
        return pygame.display.set_mode((self.getWidth(), self.getHeight()))
