import sys
import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('YASI - Yet Another Space Invaders')

background_surface = pygame.image.load('./assets/background.png').convert()
blue = pygame.image.load('./assets/blue.png').convert()
cover = pygame.image.load('./assets/cover.png').convert()
playerLife3_red = pygame.image.load('./assets/playerLife3_red.png').convert()
playerShip = pygame.image.load('./assets/playerShip3_red.png').convert()
shipBeige_manned = pygame.image.load('./assets/shipBeige_manned.png').convert()
shipBlue_manned = pygame.image.load('./assets/shipBlue_manned.png').convert()
shipGreen_manned = pygame.image.load('./assets/shipGreen_manned.png').convert()
shipPink_manned = pygame.image.load('./assets/shipPink_manned.png').convert()
shipYellow_manned = pygame.image.load('./assets/shipYellow_manned.png').convert()


def life_player():
    cord_x = WIDTH
    cord_y = HEIGHT - 40
    count = 0
    while count < 3:
        count += 1 
        cord_x -= 40
        screen.blit(playerLife3_red, (cord_x, cord_y))

# 124 x 108
def enemy():
    num_row = 5
    num_colum = 8
    for row in range(num_row):
        for colum in range(num_colum):
            enemy_selected = [shipBeige_manned, shipBlue_manned, shipGreen_manned, shipPink_manned, shipYellow_manned]
            cord_x = 144 + (colum * 130)
            cord_y = 20 + (row * 110)
            screen.blit(enemy_selected[row], (cord_x, cord_y))

def player(player_moviment_x, player_moviment_y):
     screen.blit(playerShip, (player_moviment_x, player_moviment_y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_surface, (0,0))
   
    life_player()
    enemy()
    player(640, 640)

    pygame.display.update()
