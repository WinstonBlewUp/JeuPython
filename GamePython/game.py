import pygame
from player import Player

# classe = game
class Game:
    def __init__(self):
        # genere le joueur
        self.player = Player()
        self.pressed = {}