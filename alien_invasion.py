import sys
import pygame
from ship import Ship
from house import House
from alien import Alien
from bullet import Bullet
from settings import Settings


is_blue = False
aug_bg_color = None
is_LCTRL = False
# TODO: make a purchasing system with the scoring system


class AlienInvasion:

    is_fullscreen = None

    def __init__(self):
        pygame.init()
        global is_fullscreen
        is_fullscreen = False
        global aug_bg_color  # TODO: horrible code (global)
        self.bullets = pygame.sprite.Group()
        self.settings = Settings()
        loodiMusic = pygame.mixer.Sound("music/LoodiMusic.wav")
        pygame.mixer.Sound.play(loodiMusic)

        aug_bg_color = self.settings.bg_color_purple
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.display_name)

        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.ship = Ship(self)
        self.house = House(self)

    def _create_fleet(self):
        self.ship = Ship(self)
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        avaiable_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = avaiable_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        avaiable_space_y = (self.settings.screen_height -
                            (3 * alien_height) - ship_height)
        number_rows = avaiable_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen(aug_bg_color)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Detects presses """
        global aug_bg_color
        global is_blue
        global is_LCTRL
        global is_fullscreen  # TODO: Horrible, horrible code but it works (never use global)

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_w and is_blue:
            aug_bg_color = self.settings.bg_color_purple
            is_blue = False
        elif event.key == pygame.K_w and not is_blue:
            aug_bg_color = self.settings.bg_color_blue
            is_blue = True
            """ Quit and fullscreen code """
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_LCTRL:
            is_LCTRL = True
            print(is_LCTRL)
            print("Above is once set to true")
        if event.key == pygame.K_f and is_LCTRL:
            if not is_fullscreen:
                """ Set display to fullscreen mode """
                self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                self.settings.screen_width = self.screen.get_rect().width
                self.settings.screen_length = self.screen.get_rect().height
                is_fullscreen = True
                print(is_LCTRL)
                print("this will probably never show")
        if event.key == pygame.K_f and not is_LCTRL:
            if is_fullscreen:
                """ Set display to normal mode """
                self.screen = pygame.display.set_mode(
                    (self.settings.screen_width, self.settings.screen_height))
                is_fullscreen = False

    def _check_keyup_events(self, event):
        global is_LCTRL
        """ Detects releases """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_LCTRL:
            is_LCTRL = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):

        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)  # If the first bool = false, the bullet won't disapear
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        #if pygame.sprite.spritecollideany(self.settings.screen_height - 800, self.aliens):
            #sys.exit()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            sys.exit()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self, a_bg_color):
        # Fills the screen with bg_color on every loop
        self.screen.fill(a_bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Redraws the most recent screen (gives us "movement")
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
