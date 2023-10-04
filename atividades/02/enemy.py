import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        file_path = './assets/ship' + color + '_manned.png'
        image = pygame.image.load(file_path).convert_alpha()
        self.image = pygame.transform.scale(image, (75, 75))
        self.rect = self.image.get_rect(topleft = (x,y))

        #score
        if color == 'Yellow' : self.value = 500
        elif color == 'Pink' : self.value = 400
        elif color == 'Green' : self.value = 300
        elif color == 'Blue' : self.value = 200
        elif color == 'Beige' : self.value = 100

    def update(self, direction):
        self.rect.x += direction
        
        
      


