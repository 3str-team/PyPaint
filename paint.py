import pygame
from Canvas import Canvas

displaySize = (800, 800)

pygame.init()
window = pygame.display.set_mode()

colors = [(255, 0, 0), (0, 255, 0), ((0, 0, 255))]

canvas = Canvas(window, colors)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        canvas.drawing(event)

    canvas.render()

    pygame.display.flip()