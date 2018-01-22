import pygame
import sys

def check_events():
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_setting , screen , ship):
    # 设置背景颜色
    screen.fill(ai_setting.backgroudColor)
    # 显示飞船
    ship.biltme()
    # 让最近的绘制屏幕可见
    pygame.display.flip()

