import pygame
from projectile import Projectile

#premiere classe = joueur

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity_X = 1
        self.velocity_Y = 15
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 300

    def launch_projectile(self):
        #creer instance class projectile
        self.all_projectiles.add(Projectile(self))


    def move_right(self):
        self.rect.x += self.velocity_X

    def move_left(self):
        self.rect.x -= self.velocity_X







