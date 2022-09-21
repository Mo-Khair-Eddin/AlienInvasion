import pygame


class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Ship image location
        self.image = pygame.image.load("images/ship_blue-removebg-preview.png")
        self.rect = self.image.get_rect()
        # init location
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a decimal for the ship's x-axis position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

# TODO: Maybe add the delay library and make the ship go faster the logner the game goes on
    def update(self):
        from alien_invasion import AlienInvasion
        if 1 == 2:  # is_fullscreen:
            fullscreen_movement = self.rect.y > 50
        else:
            fullscreen_movement = self.rect.y > 4
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # if self.moving_up and self.rect.y < self.screen_rect.y:
        # TODO: change how far the ship can move once in fullscreen ########################
        if self.moving_up and fullscreen_movement:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.y < self.screen_rect.y + self.settings.screen_height - 50:
            # TODO: HORRIBLE HORRIBLE code, but it works
            self.y += self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
