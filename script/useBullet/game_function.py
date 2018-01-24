import pygame
import sys
from classes.Bullet import Bullet

def check_events():
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            sys.exit()

# 点击之后单次运动
def check_events(ship):
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            sys.exit()
        # 左右移动飞船
        elif even.type == pygame.KEYDOWN:
            if even.key == pygame.K_RIGHT:
                ship.rect.centerx +=1
            elif even.key == pygame.K_LEFT:
                ship.rect.centerx -=1

# 点击之后持续运动
def check_events_keepMove(ship, setting  , bullets , screen):
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            sys.exit()
        # 左右移动 , 按下按键
        elif even.type == pygame.KEYDOWN:
            check_key_down(ship, setting , even , bullets , screen)
        # 左右移动时抬起按键
        elif even.type == pygame.KEYUP:
            check_key_up(ship,even)

# key按键按下
def check_key_down(ship , setting , even , bullets , screen):
    if even.key == pygame.K_RIGHT:
        ship.move_right = True
    elif even.key == pygame.K_LEFT:
        ship.move_left = True
    elif even.key == pygame.K_SPACE:
        new_bullet = Bullet(setting , screen , ship)
        bullets.add(new_bullet)

# key按键抬起
def check_key_up(ship , even):
    if even.key == pygame.K_RIGHT:
        ship.move_right = False
    if even.key == pygame.K_LEFT:
        ship.move_left = False


def update_screen(ai_setting , screen , ship , bullets):
    # 设置背景颜色
    screen.fill(ai_setting.backgroudColor)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 显示飞船
    ship.biltme()
    # 让最近的绘制屏幕可见
    pygame.display.flip()

