import pygame
from conf.setting import Setting
from classes.ship import Ship
from script import game_function as  gf

setting = Setting()

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((setting.width,setting.height))
    pygame.display.set_caption("Alien Invasion")
    # 创建飞船
    ship = Ship(screen)
    while True:
        gf.check_events()
        gf.update_screen(setting , screen , ship)

run_game()