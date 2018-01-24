import sys
import pygame
from conf.setting import Setting

# 创建Setting对象
setting = Setting()

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((setting.width,setting.height))
    pygame.display.set_caption("Alien Invasion")
    # 在每次执行while 循环时都绘制一个空屏幕，并擦去旧屏幕
    bg_color = setting.backgroudColor ;
    while True:
        # 设置背景颜色
        screen.fill(bg_color)
        # 只要有交互时间时,就会执行以下的for循环。例如鼠标位置的变化
        for even in pygame.event.get():
            # 点击关闭按钮 pygame.QUIT
            if even.type == pygame.QUIT:
                print("Quit Process")
                # 游戏退出
                sys.exit()
            pygame.display.flip()
run_game()
# 鼠标移动之后修改背景颜色