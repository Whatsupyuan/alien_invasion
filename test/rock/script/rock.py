import pygame


class Rock():
    def __init__(self, screen, setting):
        self.screen = screen
        self.image = pygame.image.load(
            "D:\\09_python\\python_workspace\\alien_invasion\\alien_invasion\\test\\rock\\images\\rocket.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # x轴
        self.rect.centerx = self.screen_rect.centerx
        # y轴
        self.rect.centery = self.screen_rect.centery
        # 图标放在底部
        self.rect.bottom = self.screen_rect.bottom

        # 移动flag
        self.move_down_flag = False
        self.move_up_flag = False
        self.move_left_flag = False
        self.move_right_flag = False

        # 移动速度
        self.rock_move_speed = setting.ship_speed_factor

    # 向右
    def move_right(self):
        if self.move_right_flag and self.rect.right < self.screen_rect.right :
            self.rect.centerx += self.rock_move_speed

    # 向左
    def move_left(self):
        if self.move_left_flag and self.rect.left > 0 :
            self.rect.centerx -= self.rock_move_speed

    # 向上
    def move_up(self):
        if self.move_up_flag and self.rect.top > 0 :
            self.rect.centery -= self.rock_move_speed

    # 向下
    def move_down(self):
        if self.move_down_flag and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.rock_move_speed


    def update(self):
        self.move_right()
        self.move_left()
        self.move_up()
        self.move_down()

    # 绘制内容到屏幕上
    def blitme(self):
        self.screen.blit(self.image, self.rect)
