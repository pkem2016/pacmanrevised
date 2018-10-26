import pygame.font
from pacman import Pacman

class Button():

    def __init__(self, screen, msg):

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 100, 120
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.intro_logo = pygame.image.load('images2/pacmanLogo.png')
        self.pacRight = [pygame.image.load('images2/R1.png'), pygame.image.load('images2/R2.png')]
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.pac_image = pygame.image.load('images2/newidle.png')
        self.pac_rect = self.pac_image.get_rect()
        self.b_rect = pygame.image.load('B1.png').get_rect()
        self.c_rect = pygame.image.load('C/CL1.png').get_rect()

        self.i_rect = pygame.image.load('I/I1.png').get_rect()

        self.p_rect = pygame.image.load('P/P1.png').get_rect()
        self.prep_msg(msg)

        self.speed = 1
        self.walkCount = 0
        # Get rect of the image

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.pac_rect.x = 40
        self.pac_rect.y = 300
        self.b_rect.x = 100
        self.b_rect.y = 300
        self.c_rect.x = 140
        self.c_rect.y = 300
        self.i_rect.x = 180
        self.i_rect.y = 300
        self.p_rect.x = 220
        self.p_rect.y = 300
        self.center_horizontal = float(self.pac_rect.centerx)
        self.center_vertical = float(self.pac_rect.centery)
        self.p_hor = float(self.p_rect.centerx)
        self.c_hor = float(self.c_rect.centerx)
        self.i_hor = float(self.i_rect.centerx)
        self.b_hor = float(self.b_rect.centerx)

    def prep_msg(self, msg):

        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.screen.blit(self.intro_logo, (110, 250))

    def draw_button(self):
       # self.screen.blit(self.pac_image, self.pac_rect)
        self.screen.fill(self.button_color, self.rect)
        self.moving_right = True
        if self.moving_right:
            self.screen.blit((self.pacRight[self.walkCount % 2]), self.pac_rect)
            self.walkCount += 1
            self.screen.blit(pygame.image.load('P/P1.png'), self.p_rect)

            self.screen.blit(pygame.image.load('C/CL1.png'), self.c_rect)

            self.screen.blit(pygame.image.load('B1.png'), self.b_rect)

            self.screen.blit(pygame.image.load('I/I1.png'), self.i_rect)
        self.center_horizontal += self.speed
        self.p_hor += self.speed
        self.p_rect.centerx = self.p_hor

        self.i_hor += self.speed
        self.i_rect.centerx = self.i_hor

        self.c_hor += self.speed
        self.c_rect.centerx = self.c_hor

        self.b_hor += self.speed
        self.b_rect.centerx = self.b_hor
        self.pac_rect.centerx = self.center_horizontal

        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.intro_logo, (110, 150))






