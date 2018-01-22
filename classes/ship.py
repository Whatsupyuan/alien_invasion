import pygame

class Ship():
    def __init__(self , screen):
        self.screen = screen

        # 加载 ship 图像，并获取其外接矩形
        self.image = pygame.image.load("D:\\09_python\python_workspace\\alien_invasion\\alien_invasion\\images\\ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新ship ， 放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def biltme(self):
        # 在指定位置绘制ship
        self.screen.blit(self.image , self.rect)