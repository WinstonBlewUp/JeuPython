import pygame

# def class projectile du joueur
class Projectile(pygame.sprite.Sprite):

    # def le constructeur de la class
    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('assets2/projectile.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 65
        self.rect.y = player.rect.y + 38
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #rotation
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #verif si projectile en collision avec monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supp projectile
            self.remove()
            #infliction degats
            monster.damage(self.player.attack)

        #verif si projectile hors ecran
        if self.rect.x > 630:
            #supp le projectile
            self.remove()



