#Drawing shapes
#Learn how to draw basic shapes like rectangles, circles, and lines on the screen.

import pygame
pygame.init()

screen = pygame.display.set_mode((500,400))
pygame.display.set_caption('Drawing Shapes')
running = True
while running:
    screen.fill((0, 128, 255))  # Fill the screen with blue color

    pygame.draw.rect(screen,(255, 0, 0),(50, 50, 100, 60))  # Red rectangle
    pygame.draw.circle(screen, (0, 255, 0), (300, 200), 40)        # Green circle
    pygame.draw.line(screen, (0, 0, 255), (0, 0), (500, 400), 5)   # Blue diagonal line

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
