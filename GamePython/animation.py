import pygame

#def class animation
class AnimateSprite(pygame.sprite.Sprite):

    #def des animations
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')



