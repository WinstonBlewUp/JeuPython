import pygame
from player import Player
from monster import Monster

# classe = game
class Game:

    def __init__(self):
        #definir si le jeu commence
        self.is_playing = False
        # genere le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        #remet le jeu à 0
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # appliquer img joueur
        screen.blit(self.player.image, self.player.rect)

        # actualisation de la JDV joueur
        self.player.update_health_bar(screen)

        # recup les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # appliquer img groupe projectile
        self.player.all_projectiles.draw(screen)

        # appliquer image grp monstre
        self.all_monsters.draw(screen)

        # verif direction joueur
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 500:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
