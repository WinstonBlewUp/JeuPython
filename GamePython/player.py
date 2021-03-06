import pygame
from projectile import Projectile
import animation

#premiere classe = joueur

class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity_X = 5
        self.velocity_Y = 15
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le jouer est K.O
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):

        #Jauge De Vie

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 15, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface,(111, 210, 46), [self.rect.x  + 15, self.rect.y - 10, self.health, 5])

    def launch_projectile(self):
        #creer instance class projectile
        self.all_projectiles.add(Projectile(self))
        self.start_animation()
        #jouer le son
        self.game.sound_manager.play('tir')

    def move_right(self):
        #uniquement si le joueur n'est pas en collision
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity_X


    def move_left(self):
        self.rect.x -= self.velocity_X








