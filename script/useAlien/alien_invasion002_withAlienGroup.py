import pygame
from conf.setting import Setting
from classes.ship_changeSpeed import Ship
from script.useAlien import game_function as  gf
from pygame.sprite import Group
from classes.alien import Alien

setting = Setting()


def run_game():
    screen = init_pygame()
    # 创建飞船
    ship = Ship(screen, setting)
    # 存储子弹的编组
    bullets = Group()
    # alien
    # alien = Alien(setting , screen)
    aliens = Group()
    gf.create_fleet(setting, screen, aliens, ship)

    while True:
        # 点击按键之后不动使飞机能够一直移动
        gf.check_events_keepMove(ship, setting, bullets, screen)
        ship.update()
        # bullet位置变动
        gf.update_bullet(bullets, aliens)
        gf.update_alien(aliens, setting)
        # print(len(bullets))
        gf.update_screen(setting, screen, ship, bullets, aliens)


# 重构初始化 pygame
def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((setting.width, setting.height))
    pygame.display.set_caption("Alien Invasion")
    return screen


# 运行
run_game()
