import pygame
from pygame.sprite import Sprite

'''alien类'''


class Alien(Sprite):
    def __init__(self, setting, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.setting = setting

        self.image = pygame.image.load(
            "D:\\09_python\\python_workspace\\alien_invasion\\alien_invasion\\images\\alienship3.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        # 向右移动外星人
        self.x += (self.setting.alien_speed_factor * self.setting.fleet_direction)
        self.rect.x = self.x

    def check_dege(self):
        screen_rect = self.screen.get_rect()
        if (self.rect.right >= screen_rect.right):
            return True
        elif self.rect.left <= 0:
            return True
