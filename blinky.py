import pygame
from pygame.sprite import Sprite
from settings import Settings

class Ghost(Sprite):
    def __init__(self, screen, maze, sb):
        super(Ghost, self).__init__()

        self.screen = screen

        self.ghost_idle = pygame.image.load('B1.png')
        self.ghost_up = pygame.image.load('B1.png')
        self.ghost_down = pygame.image.load('B1.png')
        self.ghost_left = pygame.image.load('B1.png')
        self.ghost_right = pygame.image.load('B1.png')
        self.rect = self.ghost_idle.get_rect()
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.walkCount = 0

        self.rect.x = 306
        self.rect.y = 306

    def blitme(self):
        """Draw pacman at its current location."""
       # self.screen.blit(self.pacman_idle, self.rect)

        if self.moving_right:
            self.screen.blit(self.ghost_right[self.walkCount % 2], self.rect)
            self.walkCount += 1

        elif self.moving_left:
            self.screen.blit(self.ghost_left[self.walkCount % 2], self.rect)
            self.walkCount += 1

        elif self.moving_up:
            self.screen.blit(self.ghost_up[self.walkCount % 2], self.rect)
            self.walkCount += 1

        elif self.moving_down:
            self.screen.blit(self.ghost_down[self.walkCount % 2], self.rect)
            self.walkCount += 1

        else:
            self.screen.blit(self.ghost_idle, self.rect)