import pygame
from pygame.sprite import Sprite
from settings import Settings
from game_stats import GameStats
#from scoreboard import Scoreboard

class Pacman(Sprite):

    def __init__(self, screen, maze, sb):
        """Initialized values"""
        super(Pacman, self).__init__()
        self.screen = screen
       # self.sb = Scoreboard()
        self.set = Settings()

        self.stats = GameStats(self.set)
        self.eatsound = pygame.mixer.Sound("sounds/munch1.wav")
        # get the rect of the screen
        self.screen_rect = screen.get_rect()
        self.sb = sb
        self.bricks = maze.bricks
        self.pellets = maze.pellets
        # Load the images for pacman
        self.pacRight = [pygame.image.load('images2/R1.png'), pygame.image.load('images2/R2.png')]
        self.pacLeft = [pygame.image.load('images2/L1.png'), pygame.image.load('images2/L2.png')]
        self.pacUp = [pygame.image.load('images2/U1.png'), pygame.image.load('images2/U2.png')]
        self.pacDown = [pygame.image.load('images2/D1.png'), pygame.image.load('images2/D2.png')]
        self.pacman_idle = pygame.image.load('images2/newidle.png')
        self.score = 0
        # Pacman speed
        self.speed = .3

        # Get rect of the image
        self.rect = self.pacman_idle.get_rect()

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.walkCount = 0

        # Initial placement of pacman
        self.rect.x = 285
        self.rect.y = 485

        # center of the sprite
        self.center_horizontal = float(self.rect.centerx)
        self.center_vertical = float(self.rect.centery)

      #  y = 400
      #  speed = .1

    def points_gathered(self):
        font = pygame.font.SysFont(None, 50)
        text = font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(text, (10, 670))

    def update(self):
        for brick in self.bricks:
            if brick.colliderect(self.rect):
                if self.moving_left:
                    self.center_horizontal += self.speed
                    self.moving_left = False
                if self.moving_right:
                    self.center_horizontal -= self.speed
                    self.moving_right = False
                if self.moving_down:
                    self.center_vertical -= self.speed
                    self.moving_down = False
                if self.moving_up:
                    self.center_vertical += self.speed
                    self.moving_up = False
                #self.center_horizontal -=1


        for pellet in self.pellets:
          #  collisions = pellet.colliderect(self.rect)
          #  if collisions:
          #      for pellet in collisions.value():

            if pellet.colliderect(self.rect):
                self.stats.score += self.set.pellet_points * len(pellet)
               # self.prep_score()
                self.score +=10
                pygame.mixer.Sound.play(self.eatsound)
                self.pellets.remove(pellet)


        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_horizontal += self.speed
            print( self.rect.x, self.rect.y)
        if self.moving_left and self.rect.right < self.screen_rect.right:
            self.center_horizontal -= self.speed
            print( self.rect.x, self.rect.y)
        if self.moving_up and self.rect.right < self.screen_rect.right:
            self.center_vertical -= self.speed
            print( self.rect.x, self.rect.y)
        if self.moving_down and self.rect.right < self.screen_rect.right:
            self.center_vertical += self.speed
            print( self.rect.x, self.rect.y)
        self.rect.centerx = self.center_horizontal
        self.rect.centery = self.center_vertical


    def blitme(self):
        """Draw pacman at its current location."""
       # self.screen.blit(self.pacman_idle, self.rect)

        if self.moving_right:
            self.screen.blit(self.pacRight[self.walkCount % 2], self.rect)
            self.walkCount += 1

        elif self.moving_left:
            self.screen.blit(self.pacLeft[self.walkCount % 2], self.rect)
            self.walkCount += 1

        elif self.moving_up:
            self.screen.blit(self.pacUp[self.walkCount % 2], self.rect)
            self.walkCount += 1

        elif self.moving_down:
            self.screen.blit(self.pacDown[self.walkCount % 2], self.rect)
            self.walkCount += 1

        else:
            self.screen.blit(self.pacman_idle, self.rect)

