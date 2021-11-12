import pygame
from comet import Comet

#créer une classe qui gère comet event

class CometFallEvent:

    #créer compteur -> chrg bar
    def __init__(self,game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False

        #def groupe de sprite pour cometfall
        self.all_comets = pygame.sprite.Group()


    def add_percent(self):
        self.percent += (self.percent_speed / 100)

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        #boucle pour valeur (1, 10)
        for i in range(1, 10):
            #apparition boule de feu
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        #la jauge est au max
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("pluie comètes")
            self.meteor_fall()
            self.fall_mode = True

    def update_bar(self, surface):
        # ajout percent bar
        self.add_percent()



        #barre noire bg
        pygame.draw.rect(surface, (0, 0, 0), [
            0,
            surface.get_height() - 20,
            surface.get_width(),
            10
        ])
        #barre rouge fg
        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() - 20,
            (surface.get_width() / 100) * self.percent,
            10
        ])
