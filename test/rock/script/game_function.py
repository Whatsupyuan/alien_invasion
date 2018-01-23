import sys
import pygame

def moveIco(rock):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rock.move_right_flag = True
            if event.key == pygame.K_LEFT:
                rock.move_left_flag = True
            if event.key == pygame.K_UP:
                rock.move_up_flag = True
            if event.key == pygame.K_DOWN:
                rock.move_down_flag = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rock.move_right_flag = False
            if event.key == pygame.K_LEFT:
                rock.move_left_flag = False
            if event.key == pygame.K_UP:
                rock.move_up_flag = False
            if event.key == pygame.K_DOWN:
                rock.move_down_flag = False