import pygame
from conf.setting import Setting
from classes.ship_changeSpeed import Ship
from script import game_function as  gf

setting = Setting()

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((setting.width,setting.height))
    pygame.display.set_caption("Alien Invasion")
    # 创建飞船
    ship = Ship(screen , setting)
    while True:
        # 点击按键之后不动使飞机能够一直移动
        gf.check_events_keepMove(ship)
        ship.update()
        gf.update_screen(setting , screen , ship)

run_game()