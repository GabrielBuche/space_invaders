import sys
import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('YASI - Yet Another Space Invaders')

# background
background_surface = pygame.image.load('./assets/background.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_surface, (0,0))

    pygame.display.update()
