import pygame
import sys

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
def check_events_keepMove(ship):
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            sys.exit()
        # 左右移动 , 按下按键
        elif even.type == pygame.KEYDOWN:
            if even.key == pygame.K_RIGHT:
                ship.move_right = True
            elif even.key == pygame.K_LEFT:
                ship.move_left = True
        # 左右移动时抬起按键
        elif even.type == pygame.KEYUP:
            if even.key == pygame.K_RIGHT:
                ship.move_right = False
            if even.key == pygame.K_LEFT:
                ship.move_left = False


def update_screen(ai_setting , screen , ship):
    # 设置背景颜色
    screen.fill(ai_setting.backgroudColor)
    # 显示飞船
    ship.biltme()
    # 让最近的绘制屏幕可见
    pygame.display.flip()

