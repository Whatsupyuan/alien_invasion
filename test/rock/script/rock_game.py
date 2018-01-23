import pygame
import game_function as gf

from test.rock.script.rock import Rock
from conf.setting import Setting

def game_main():
    pygame.init()
    screen = pygame.display.set_mode((800,400))
    pygame.display.set_caption("Rock")
    backgroud_color = (230,230,230) ;

    setting = Setting()

    rock = Rock(screen,setting)
    while True:
        screen.fill(backgroud_color)
        gf.moveIco(rock)
        rock.update()
        rock.blitme()
        pygame.display.flip()

game_main()
