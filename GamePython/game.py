import pygame
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent

# classe = game
from sounds import SoundManager


class Game:

    def __init__(self):
        #definir si le jeu commence
        self.is_playing = False
        # genere le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #gen manager event (cometfall)
        self.comet_event = CometFallEvent(self)
        #groupe monstre
        self.all_monsters = pygame.sprite.Group()
        #gerer le son
        self.sound_manager = SoundManager()
        #initialiser le score 0
        self.score = 0
        self.pressed = {}



    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points = 10):
        self.score += points

    def game_over(self):
        #remet le jeu à 0
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        #jouer le son
        self.sound_manager.play('game_over')

    def update(self, screen):

        #aff score sur l'écran
        font = pygame.font.SysFont("monospace", 16)
        score_text = font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # appliquer img joueur
        screen.blit(self.player.image, self.player.rect)

        # actualisation de la JDV joueur
        self.player.update_health_bar(screen)

        # actualiser la barre event du jeu
        self.comet_event.update_bar(screen)

        # actualiser animation joueur
        self.player.update_animation()

        # recup les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        #recup comet
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer img groupe comets
        self.comet_event.all_comets.draw(screen)

        # appliquer img groupe projectile
        self.player.all_projectiles.draw(screen)

        # appliquer image grp monstre
        self.all_monsters.draw(screen)

        # verif direction joueur
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1200:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))
