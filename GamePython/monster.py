import pygame
import random
import animation

# def class monstre
class Monster(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 1100 + random.randint(0, 300)
        self.rect.y = 500
        self.velocity = random.randint(1, 3)
        self.start_animation()

    def damage(self, amount):
        #infliction des degat
        self.health -= amount

        #verif si PV <= 0
        if self.health <= 0:
            # respawn monstre
            self.rect.x = 1100 + random.randint(0, 300)
            self.velocity = 1
            self.health = self.max_health

            #si comet fall a 100%
            if self.game.comet_event.is_full_loaded():

                #retire du jeu
                self.game.all_monsters.remove(self)

                # appel methpde pluie
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop = True)

    def update_health_bar(self, surface):

        #Jauge De Vie

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 25, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface,(111, 210, 46), [self.rect.x + 25, self.rect.y - 10, self.health, 5])


    def forward(self):
        #uniquement si pas collision joueur(groupe)
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si en collision
        else:
            #infliction degats
            self.game.player.damage(self.attack)