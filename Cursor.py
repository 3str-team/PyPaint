import pygame


class Cursor:

    def __init__(self, window, size, color, type="draw"):
        self.__window = window
        self.__pos = (0, 0)
        self.__size = size
        self.__color = color

    def setPosition(self, pos):
        self.__pos = pos

    def setSize(self, size):
        self.__size = size

    def setColor(self, color):
        self.__color = color

    def render(self):
        pygame.draw.circle(self.__window, self.__color, self.__pos,
                           self.__size)

        pygame.draw.circle(self.__window, (0, 0, 0), self.__pos, self.__size,
                           1)
