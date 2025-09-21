import pygame
pygame.init()


screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('Background Music')


#load and play background music
pygame.mixer.init()
pygame.mixer.music.load("one-piece-mania_we-are.mp3")#use file open dialog box to select file
pygame.mixer.music.play(-1)#loop indefinitely


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            exit()
