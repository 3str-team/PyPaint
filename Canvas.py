import pygame
from Line import Line
from Cursor import Cursor
from Color import Color


class Canvas:

    def __init__(self, window, colors=[]):
        self.window = window
        self.color = (255, 0, 0)
        self.bgColor = (0, 0, 0)
        self.width = 1
        self.lines = []
        self.currentLine = Line(window, self.color, self.width)
        self.__colors = {
            "current": 0,
            "list": [Color(window, color) for color in colors]
        }

        self.selectCurrentColor()

        self.isMoving = False
        self.lastMousePosition = (0, 0)

        self.Cursor = Cursor(self.window, self.width / 2, self.color)

    def mouseWheelHandler(self, event):
        if event.button == 4:
            self.width = max(self.width - 1, 1)
        elif event.button == 5:
            self.width += 1

        self.Cursor.setSize(self.width / 2)
        self.currentLine.setWidth(self.width)

    def checkSwithColor(self, pos):
        result = False
        self.unselectCurrentColor()
        for i in range(len(self.__colors["list"])):
            if self.__colors["list"][i].getRect().collidepoint(pos):
                self.__colors["current"] = i
                result = self.__colors["list"][i].getColor()
                break

        self.selectCurrentColor()
        return result

    def unselectCurrentColor(self):
        self.__colors["list"][self.__colors["current"]].unselect()

    def selectCurrentColor(self):
        self.__colors["list"][self.__colors["current"]].select()

    def changeColorHandler(self):
        self.Cursor.setColor(self.color)

    def drawing(self, event):
        self.window.fill(self.bgColor)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.isMoving:
                    self.lastMousePosition = event.pos
                else:
                    swithColor = self.checkSwithColor(event.pos)
                    if swithColor:
                        self.color = swithColor
                        self.changeColorHandler()
                    else:
                        self.currentLine.addPoint(event.pos)
            if event.button == 4 or event.button == 5:
                self.mouseWheelHandler(event)
        elif event.type == pygame.MOUSEMOTION:
            self.Cursor.setPosition(event.pos)
            if event.buttons[0]:
                if self.isMoving:
                    self.moveCanvas(event.pos[0] - self.lastMousePosition[0],
                                    event.pos[1] - self.lastMousePosition[1])
                    self.lastMousePosition = event.pos
                else:
                    self.currentLine.addPoint(event.pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.lines.append(self.currentLine)
                self.currentLine = Line(self.window, self.color, self.width)

        self.movingHandler(event)

    def movingHandler(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
            self.isMoving = True

        if event.type == pygame.KEYUP and event.key == pygame.K_LCTRL:
            self.isMoving = False

    def moveCanvas(self, deltaX, deltaY):
        for line in self.lines:
            line.move(deltaX, deltaY)

    def renderColors(self):
        if len(self.__colors):
            padding = 10
            colorSize = self.__colors["list"][0].getSize()
            for i in range(len(self.__colors["list"])):
                self.__colors["list"][i].setPosition(
                    (padding * (i + 1) + colorSize * i, padding))
                # print((padding * (i + 1) + colorSize * i, padding))
                self.__colors["list"][i].render()

    def render(self):

        for line in self.lines:
            line.render()

        self.currentLine.render()

        self.Cursor.render()

        self.renderColors()
