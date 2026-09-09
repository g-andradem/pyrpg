# Contains all sprites (player, enemies, map, ..)
# + also deals with their interactions
# needs to be able to manage hundreds of sprites effectively
# via groups

import pygame

class Level:
    def __init__(self):
        #get the display surface
        self.display_surface = pygame.display.get_surface()

        # Sprite group Setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

    def run(self):
        #update and draw the game
        pass