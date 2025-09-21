#Handling Keyboard and Mouse Events
#React when a user presses a key or clicks the mouse.

import pygame
pygame.init()

win = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Key & Mouse Events")

running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print("Key Pressed:", pygame.key.name(event.key))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse Clicked at:", event.pos)

pygame.quit()
