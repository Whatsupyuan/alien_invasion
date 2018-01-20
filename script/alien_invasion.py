import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    # 在每次执行while 循环时都绘制一个空屏幕，并擦去旧屏幕
    while True:
        for even in pygame.event.get():
            # 点击关闭按钮 pygame.QUIT
            if even.type == pygame.QUIT:
                print("Quit Process")
                # 游戏退出
                sys.exit()
        pygame.display.flip()

run_game()

# 鼠标移动之后修改背景颜色