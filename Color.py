import pygame


class Color:

    def __init__(self, window, color, pos=[0, 0]):
        self.__window = window
        self.__color = color
        self.__pos = pos
        self.__size = 25
        self.__rect = pygame.Rect(pos[0], pos[1], self.__size, self.__size)

        self.__isSelect = False

    def setPosition(self, pos):
        if pos[0] != self.__pos[0] or pos[1] != self.__pos[1]:
            self.__pos = pos
            self.__rect = pygame.Rect(pos[0], pos[1], self.__size, self.__size)
            print(self.__pos)

    def getSize(self):
        return self.__size

    def getRect(self):
        return self.__rect

    def getColor(self):
        return self.__color

    def select(self):
        self.__isSelect = True

    def unselect(self):
        self.__isSelect = False

    def render(self):
        pygame.draw.rect(self.__window, self.__color, self.__rect, 0, 5)
        pygame.draw.rect(self.__window, (0, 0, 0), self.__rect, 2, 5)

        if self.__isSelect:
            pygame.draw.rect(self.__window, (230, 230, 230), self.__rect, 2, 5)
