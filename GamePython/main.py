import pygame
from game import Game
from player import Player
pygame.init()


#gen enetre du jeu

pygame.display.set_caption("Sheriff Vs Alien")
screen = pygame.display.set_mode((626, 417))

#import bg
background = pygame.image.load('assets/bg.jpg')

#chargement du jeu
game = Game()


running = True
is_jump = False
#boucle running fentre ouverte

while running:

    #appliquer le bg
    screen.blit(background,(0, 0))

    #appliquer img joueur
    screen.blit(game.player.image, game.player.rect)

    # recup les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()
    #appliquer img groupe projectile
    game.player.all_projectiles.draw(screen)

    #verif direction joueur
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 500:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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

