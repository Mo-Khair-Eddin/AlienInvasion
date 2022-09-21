class Settings:

    def __init__(self):
        self.display_name = "Super Duper Cool Alien Invasion Game (Arrow Keys = move. Space = shoot. E = change bg)"
        self.screen_width = 1440
        self.screen_height = 800
        self.bg_color_purple = (200, 200, 255)
        self.bg_color_blue = (95, 252, 255)
        # Ship settings:
        self.ship_speed = 1.5
        # Bullet settings:
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 5
        self.bullet_color = (60, 60, 60)
        # Alien settings:
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 1 = right & -1 = left
        self.fleet_direction = 1