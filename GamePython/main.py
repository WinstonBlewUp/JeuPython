import pygame
import math
from game import Game
from player import Player
pygame.init()


#gen enetre du jeu

pygame.display.set_caption("Shooter")
screen = pygame.display.set_mode((1080, 720))

#import bg
background = pygame.image.load('assets/bg.jpg')

#chargement banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# import bouton PLAY
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (500, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 4 + 10 )
play_button_rect.y = math.ceil(screen.get_height() / 2)
#chargement du jeu
game = Game()


running = True
is_jump = False
#boucle running fentre ouverte

while running:

    #appliquer le bg
    screen.blit(background,(0, -200))

    #verif si le jeu a commence
    if game.is_playing:
        #declenchement des instructions du jeu
        game.update(screen)
    #verif si le jeu n'a pas commence
    else:
        #ajout ecran accueil
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    #MaJ ecran
    pygame.display.flip()

    # condition sortie (fenetre fermee)
    for event in pygame.event.get():
        #verif element fermeture
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        #detect lache touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detect touche espace pour jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_jump = True
                if is_jump:
                    #pygame.time.delay(0)
                    game.player.rect.y -= game.player.velocity_Y
                    game.player.velocity_Y -= 1
                    if game.player.velocity_Y <= -15 and game.player.rect.y <= 300:
                        is_jump = False
                        game.player.velocity_Y = 14
                        if  is_jump is False:
                            game.player.rect.y = 300

            #detect touche s pour shoot
            if event.key == pygame.K_s:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verif si collision avec btn PLAY
            if play_button_rect.collidepoint(event.pos):
                # lancer le jeu
                game.start()

