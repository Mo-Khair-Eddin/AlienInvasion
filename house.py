import pygame

class House:

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Ship image location
        self.image = pygame.image.load("images/house.bmp")
        self.rect = self.image.get_rect()
        # init location
        self.rect.midbottom = self.screen_rect.midbottom