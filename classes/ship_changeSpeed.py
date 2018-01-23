import pygame

'''
添加可以变速移动飞船的属性
setting类通过参数传递过来时,不需要告知setting类位置,只当对象传递,传递之后直接使用
'''
class Ship():
    def __init__(self , screen , setting):
        self.screen = screen

        # 加载 ship 图像，并获取其外接矩形
        self.image = pygame.image.load("D:\\09_python\python_workspace\\alien_invasion\\alien_invasion\\images\\ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新ship ， 放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 左右移动标识
        self.move_right = False
        self.move_left = False

        # 飞船的位置
        self.center = float(self.rect.centerx)
        self.global_setting = setting

    def biltme(self):
        # 在指定位置绘制ship
        self.screen.blit(self.image , self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right :
            self.center += self.global_setting.ship_speed_factor
        if self.move_left and self.rect.left>0:
            self.center -= self.global_setting.ship_speed_factor

        self.rect.centerx = self.center