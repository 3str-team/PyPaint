import pygame


class Line:

    def __init__(self, window, color, width):
        self.__window = window
        self.__points = []
        self.__color = color
        self.__width = width

    def addPoint(self, point):
        self.__points.append(list(point))

    def setWidth(self, width):
        self.__width = width

    def move(self, deltaX, deltaY):
        for i in range(len(self.__points)):
            self.__points[i][0] += deltaX
            self.__points[i][1] += deltaY

    def render(self):
        if len(self.__points) > 1:
            pygame.draw.lines(self.__window, self.__color, False,
                              self.__points, self.__width)

        for point in self.__points:
            pygame.draw.circle(self.__window, self.__color, point,
                               self.__width / 2 * 0.83)
