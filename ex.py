import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.draw.circle(screen, (255,0,0), (25,81), 80,  width = 0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
