class Settings():
    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (0, 0, 0)
        self.ship_limit = 2
        self.fleet_drop_speed = 3
        self.fleet_direction = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        self.bullet_allowed = 30
        self.laser_allowed = 12
        self.speedup_scale = 1.05
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.pause_count = 2
        self.pellet_points = 50

    def increase_speed(self):

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
