import pygame
import random

#class gerer comete
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        #def quelle est l'image  comet
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        #jouer le son
        self.comet_event.game.sound_manager.play('meteorite')

        #verif si le nbr de comet == 0
        if len(self.comet_event.all_comets) == 0:
            print("event terminé")
            #remettre barre à 0
            self.comet_event.reset_percent()
            #apparaitre les montres
            self.comet_event.game.start()


    def fall(self):
        self.rect.y += self.velocity

        #ne tombe pas sur le sol
        if self.rect.y >= 500:
            print("contact au sol")

            #retirer la boule de feu
            self.remove()

            #verif s'il reste des boules en jeu
            if len(self.comet_event.all_comets) == 0:
                print("event fini")
                #remettre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # verif si boule de feu touche le joueur
        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_players
        ):
            print("joueur touché")
            #remove bdf
            self.remove()
            #subir degats joueur
            self.comet_event.game.player.damage(20)