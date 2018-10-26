import pygame
import sys
import scoreboard as sb

class EventLoop:
    def __init__(self, finished):
        self.finished = finished

    def __str__(self):
        return 'eventloop, finished=' + str(self.finished) + ')'


    @staticmethod
    def check_events(screen, player, sb, play_button, stats, set):

        screen_rect = screen.get_rect()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, player, stats, play_button)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(stats, sb, play_button, mouse_x, mouse_y, set)
#            elif event.type == pygame.KEYUP:
#                check_keyup_events(event, player)

def check_keydown_events(event, player, stat, play_button):

        if event.key == pygame.K_RIGHT:
                player.moving_right = True
                player.moving_left  = False
                player.moving_up    = False
                player.moving_down  = False
        if event.key == pygame.K_LEFT:
                player.moving_left = True
                player.moving_right = False
                player.moving_up = False
                player.moving_down = False
        if event.key == pygame.K_UP:
                player.moving_up = True
                player.moving_down = False
                player.moving_left = False
                player.moving_right = False
        if event.key == pygame.K_DOWN:
                player.moving_down = True
                player.moving_up = False
                player.moving_left = False
                player.moving_right = False
        if event.key == pygame.K_RETURN:
            if set.pause_count == 2:

                set.initialize_dynamic_settings()

                pygame.mouse.set_visible(False)

                stat.reset_stats()
                stat.game_active = True
                pygame.mouse.set_visible(True)

                sb.prep_score()
                sb.prep_high_score()
                sb.prep_level()
                sb.prep_ships()


            elif (set.pause_count % 2) == 0:
                pygame.mouse.set_visible(False)
                stat.game_active = True

            else:

                pygame.mouse.set_visible(True)
                stat.game_active = False
                play_button.draw_button()
            set.pause_count += 1


def check_play_button( stats, sb, play_button, mouse_x, mouse_y, set):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        if set.pause_count <= 2:
            set.initialize_dynamic_settings()
            pygame.mouse.set_visible(False)

            stats.reset_stats()
            stats.game_active = True
            pygame.mouse.set_visible(True)

            sb.prep_score()
            sb.prep_high_score()
            sb.prep_level()
            sb.prep_ships()

        else:
            pygame.mouse.set_visible(False)
            stats.game_active = True


#def check_keyup_events(event, player):
#        if event.key == pygame.K_RIGHT:
#                player.moving_right = False

#        if event.key == pygame.K_LEFT:
#                player.moving_left = False
#        if event.key == pygame.K_UP:
#                player.moving_up = False
#        if event.key == pygame.K_DOWN:
#                player.moving_down = False
