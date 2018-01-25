import pygame
from pygame.sprite import Sprite
'''alien类'''
class Alien(Sprite):
    def __init__(self , setting , screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.setting = setting

        self.image = pygame.image.load("D:\\09_python\\python_workspace\\alien_invasion\\alien_invasion\\images\\alienship3.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image , self.rect)