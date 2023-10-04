import pygame, sys
from player import Player
from enemy import Enemy
from laser import Laser
from random import choice


class Game:
    def __init__(self):
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # enemy
        self.enemies = pygame.sprite.Group()
        self.enemy_laser = pygame.sprite.Group()
        self.enemy_setup(rows= 5, cols= 8)
        self.enemy_direction = 3
        
        self.score = 0

        #fonts
        self.font = pygame.font.Font('./fonts/slkscr.ttf', 18)

        #health
        self.lives = 3
        self.live_surf = pygame.image.load('./assets/playerLife3_red.png').convert_alpha()
        self.live_x_start_position = screen_width - (self.live_surf.get_size()[0] * 3 + 20)

    def enemy_setup(self, rows, cols, dist = 85, offset = 300 ):
        for index_row, row in enumerate(range(rows)):
            for index_cols, col in enumerate(range(cols)):
                x = index_cols * dist + offset
                y = index_row  * dist 

                if index_row == 0: enemy_sprite = Enemy('Yellow', x, y)
                elif index_row == 1: enemy_sprite = Enemy('Pink', x, y)
                elif index_row == 2: enemy_sprite = Enemy('Green', x, y)
                elif index_row == 3: enemy_sprite = Enemy('Blue', x, y)
                elif index_row == 4: enemy_sprite = Enemy('Beige', x, y)
       
                self.enemies.add(enemy_sprite)

    def enemy_position_check(self):
        all_enemies = self.enemies.sprites()
        for enemy in all_enemies:
            if enemy.rect.right >= screen_width:
                self.enemy_direction = -5
                self.enemy_move_down(5)
                self.fast_invader.play()
            elif enemy.rect.left <= 0:
                self.enemy_direction = 5
                self.enemy_move_down(5)
                self.fast_invader.play()

    def enemy_move_down(self, dist):
        if self.enemies:
            for enemy in self.enemies.sprites():
                enemy.rect.y +=  dist

    def enemy_shoot(self,speed_shoot= 6):
        if self.enemies.sprites():
            random_enemy = choice(self.enemies.sprites())
            laser_sprite = Laser(random_enemy.rect.center, speed_shoot, screen_height)
            self.enemy_laser.add(laser_sprite)

    def collision_check(self):
        #collision player laser
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                enemy_hit = pygame.sprite.spritecollide(laser, self.enemies, True)

                if enemy_hit:
                    for enemy in enemy_hit:
                        self.score += enemy.value
                    laser.kill()
                    self.kill_sound.play()

        # life player
        if self.enemy_laser:
            for laser in self.enemy_laser:
                if pygame.sprite.spritecollide(laser,self.player, False):
                    laser.kill()
                    self.lives -= 1
                    self.explosion_sound.play()
                    if self.lives <= 0:
                        pygame.quit()
                        sys.exit()

        # collision enemy with  player
        if self.enemies:
            for enemy in self.enemies:
                if pygame.sprite.spritecollide(enemy,self.player, False):
                    pygame.quit()
                    sys.exit()

    def display_live(self):
        for live in range(self.lives):
            x = self.live_x_start_position + (live * self.live_surf.get_size()[0] + 10)
            y = screen_height - self.live_surf.get_size()[0] - 10
            screen.blit(self.live_surf, (x, y))

    def display_score(self):
        score_surf = self.font.render(f'pontuacao: {self.score}', False, 'white')
        score_rect = score_surf.get_rect(topleft = (0,0))
        screen.blit(score_surf, score_rect)

    def run(self):
        self.player.update()
        self.enemies.update(self.enemy_direction)
        self.enemy_laser.update()

        self.enemy_position_check()
        self.collision_check()

        self.display_live()
        self.display_score()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen) 
        self.enemies.draw(screen)
        self.enemy_laser.draw(screen)

        #sound
        self.explosion_sound = pygame.mixer.Sound('./sound/explosion.wav')
        self.explosion_sound.set_volume(0.3)

        self.kill_sound = pygame.mixer.Sound('./sound/invaderkilled.wav')
        self.kill_sound.set_volume(0.2)

        self.fast_invader = pygame.mixer.Sound('./sound/fastinvader1.wav')
        self.fast_invader.set_volume(0.2)

        
if __name__ == '__main__':    
   
    pygame.init()
    pygame.mixer.init()

    screen_width = 1280
    screen_height = 720

    pygame.display.set_caption('YASI - Yet Another Space Invaders')
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    enemyLaser = pygame.USEREVENT + 1
    pygame.time.set_timer(enemyLaser, 600)

    background = pygame.image.load('./assets/background.png').convert()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == enemyLaser:
                game.enemy_shoot()
    
        screen.blit(background, (0,0))
        game.run()

        pygame.display.flip()
        clock.tick(60)
