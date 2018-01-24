import pygame
import sys

def run_function():
    pygame.init()
    screen = pygame.display.set_caption("print")
    screen = pygame.display.set_mode((800,400))

    while True:
        for event in pygame.event.get():
            screen.fill((233,233,233))
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(event.key)

        pygame.display.flip()

run_function()