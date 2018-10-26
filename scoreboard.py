import pygame.font
from pygame.sprite import Group

from pacman import Pacman
from maze import Maze

class Scoreboard():
    def __init__(self, ai_settings, screen, stats, maze):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.maze = maze
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, (0,0,0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, (0,0,0))

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True,self.text_color, (0,0,0))

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.pacmans = Group()
        for ship_number in range(self.stats.ships_left+1):
            pacman = Pacman(self.screen, self.maze, self)
            pacman.rect.x = 10 + ship_number * pacman.rect.width
            pacman.rect.y = 10
            self.pacmans.add(pacman)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #self.pacmans.draw(self.screen)
