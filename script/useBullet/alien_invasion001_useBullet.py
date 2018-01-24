import pygame
from conf.setting import Setting
from classes.ship_changeSpeed import Ship
from script.useBullet import game_function as  gf
from pygame.sprite import Group

setting = Setting()

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((setting.width,setting.height))
    pygame.display.set_caption("Alien Invasion")
    # 创建飞船
    ship = Ship(screen , setting)

    # 存储子弹的编组
    bullets = Group()

    while True:
        # 点击按键之后不动使飞机能够一直移动
        gf.check_events_keepMove(ship,setting,bullets,screen)
        ship.update()
        bullets.update()
        # 删除已经跑出屏幕顶部字段,降低程序运行消耗
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # 打印当前在 Group - Bullets 中的有效弹药
        # print(len(bullets))
        gf.update_screen(setting , screen , ship , bullets)

# 运行
run_game()