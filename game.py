import pygame
from eventloop import EventLoop
from maze import Maze
from expandfile import ExpandFile
from pacman import Pacman
from blinky import Ghost
from time import sleep
from game_stats import GameStats
from settings import Settings
from scoreboard import Scoreboard
from button import Button

class Game:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.set = Settings()
        self.screen = pygame.display.set_mode((600, 720))
        pygame.display.set_caption('Pacman')
        self.stats = GameStats(self.set)
        # Create a pacman object to pass to maze
        #sb = Scoreboard(set, self.screen, stats, self.maze)
        #self.play_button = Button(self.screen, "Start munchin'")
        # Give files needed to populate the maze
        self.expandfile = ExpandFile('test.txt', expandBy=2)
        self.maze = Maze(self.screen, 'newtest.txt', 'images/purptile4', 'images/foodPellet', 'B1', 'C/CL1', 'I/I1',
                         'P/P1')
        self.intro = pygame.mixer.Sound("sounds/pacman_beginning.wav")
        self.sb = Scoreboard(self.set, self.screen, self.stats, self.maze)
        self.player = Pacman(self.screen, self.maze, self.sb)
        self.blinky = Ghost(self.screen, self.maze, self.sb)
        self.play_button = Button(self.screen, "Start munchin'")
    # def __str__(self): return

    def play(self):
       # sleep(4)
        #pygame.mixer.Sound.play(self.intro)
        sleep(1)
        eventloop = EventLoop(finished=False)

        pygame.mixer.Sound.play(self.intro)

        while not eventloop.finished:
            #self.clock.tick(60)
            eventloop.check_events(self.screen, self.player, self.sb, self.play_button, self.stats, self.set)
            self.player.update()

            self.update_screen()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.maze.blitme()
        self.player.blitme()
        self.blinky.blitme()
        #self.sb.show_score()
        self.player.points_gathered()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()


game = Game()
game.play()
