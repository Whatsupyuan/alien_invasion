import pygame
import sys
from classes.Bullet import Bullet
from classes.alien import Alien


def check_events():
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            sys.exit()


# 点击之后单次运动
def check_events(ship):
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            sys.exit()
        # 左右移动飞船
        elif even.type == pygame.KEYDOWN:
            if even.key == pygame.K_RIGHT:
                ship.rect.centerx += 1
            elif even.key == pygame.K_LEFT:
                ship.rect.centerx -= 1


# 点击之后持续运动
def check_events_keepMove(ship, setting, bullets, screen):
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            sys.exit()
        # 左右移动 , 按下按键
        elif even.type == pygame.KEYDOWN:
            check_key_down(ship, setting, even, bullets, screen)
        # 左右移动时抬起按键
        elif even.type == pygame.KEYUP:
            check_key_up(ship, even)


# key按键按下
def check_key_down(ship, setting, even, bullets, screen):
    if even.key == pygame.K_RIGHT:
        ship.move_right = True
    elif even.key == pygame.K_LEFT:
        ship.move_left = True
    elif even.key == pygame.K_SPACE:
        shootingBullet(bullets, setting, screen, ship)
    # 按键 q 退出Game
    elif even.key == pygame.K_q:
        sys.exit()


# key按键抬起
def check_key_up(ship, even):
    if even.key == pygame.K_RIGHT:
        ship.move_right = False
    if even.key == pygame.K_LEFT:
        ship.move_left = False


def update_screen(ai_setting, screen, ship, bullets):
    # 设置背景颜色
    screen.fill(ai_setting.backgroudColor)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 显示飞船
    ship.biltme()
    # 让最近的绘制屏幕可见
    pygame.display.flip()


def update_screen(ai_setting, screen, ship, bullets, aliens):
    # 设置背景颜色
    screen.fill(ai_setting.backgroudColor)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 显示飞船
    ship.biltme()
    # alien.blitme()
    aliens.draw(screen)
    # 让最近的绘制屏幕可见
    pygame.display.flip()


# shooting
def shootingBullet(bullets, setting, screen, ship):
    # 加入子弹的限制,获取子弹额数量
    if len(bullets) < setting.bullets_allowed:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)


# 更新子弹位置
def update_bullet(bullets):
    # 更新bullet位置
    bullets.update()
    # 删除已经跑出屏幕顶部bullet,降低程序运行消耗
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_bullet(bullets, aliens):
    # 更新bullet位置
    bullets.update()
    # 删除已经跑出屏幕顶部bullet,降低程序运行消耗
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


# 创建一行 alien
def create_fleet(setting, screen, aliens, ship):
    alien = Alien(setting, screen)
    number_aliens_x = get_number_aliens_x(alien.rect.width, setting)
    number_rows = get_number_rows(setting, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(alien_number, alien.rect.width, aliens, screen, setting, row_number)


# [重构] 创建alien
def create_alien(alien_number, alien_width, aliens, screen, setting, row_number):
    alien = Alien(setting, screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


# [重构] 一行显示的 alien 数量
def get_number_aliens_x(alien_width, setting):
    available_space_x = setting.width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(setting, ship_height, alien_height):
    available_space_y = (setting.height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_alien(aliens):
    aliens.update()


def update_alien(aliens, setting):
    check_fleet_edges(setting, aliens)
    aliens.update()


def check_fleet_edges(setting, aliens):
    for alien in aliens.sprites():
        if alien.check_dege():
            change_fleet_direction(setting, aliens)
            break


def change_fleet_direction(setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += setting.fleet_drop_speed
    setting.fleet_direction *= -1
