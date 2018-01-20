import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((500,400))
    pygame.display.set_caption("Alien Invasion")
    # 在每次执行while 循环时都绘制一个空屏幕，并擦去旧屏幕
    bg_color = (189,252,201) ;
    init_num = 0 ;
    max_num = 255 ;
    while True:
        # 设置背景颜色
        #screen.fill(bg_color)
        # 只要有交互时间时,就会执行以下的for循环。例如鼠标位置的变化
        for even in pygame.event.get():
            # 点击关闭按钮 pygame.QUIT
            if even.type == pygame.QUIT:
                print("Quit Process")
                # 游戏退出
                sys.exit()
            if init_num <= max_num:
                color_list = (init_num , 255 , 255)
                screen.fill(color_list)
                print(color_list)
                init_num += 1
            else:
                init_num = 0
        print("while True循环")
        pygame.display.flip()
run_game()

# 鼠标移动之后修改背景颜色