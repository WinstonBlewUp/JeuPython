import pygame

#def class animation

class AnimateSprite(pygame.sprite.Sprite):

    #def des animations
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0 #debut anim ig n0
        self.images = animations.get(sprite_name)

    #definir une methode d'animation du sprite
    def animate(self):

        # passet a nxt img
        self.current_image += 1

        #verif si on a atteint la fin
        if self.current_image >= len(self.images):
            #remettre anim à 0
            self.current_image = 0
        #remplacer l'img de l'anim prec -> nxt
        self.image = self.images[self.current_image]


#def une fonction qui charge les images dun sprite
def load_animation_images(sprite_name):
    #charger les 24img du sprite
    images = []
    # recup chemin dossier du sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    #boucle sur chaque image du dossier
    for num in range(1, 8):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    #renvoyer le contenu liste image
    return images

#def dico contenant les images chargees des sprites
animations = {
    'monster': load_animation_images('monster')
}


