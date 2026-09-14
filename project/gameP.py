import pygame, sys
from settingsP import *
# from levelP import Level
from gameMenu import GameMenu

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Rpg')
        self.clock = pygame.time.Clock()

        # self.level = Level()
        self.gameMenu = GameMenu()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')

            self.gameMenu.run()

            # self.level.run()

            pygame.display.update()
            self.clock.tick(FPS)