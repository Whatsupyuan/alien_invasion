import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, setting, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = setting.bullet_color
        self.speed_factor = setting.bullet_speed_factor

    # 移动子弹位置
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    # 在屏幕上绘制Bullet
    def draw_bullet(self):
        pygame.draw.rect(self.screen , self.color , self.rect)
