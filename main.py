import pygame
import square
from sys import exit

pygame.init()

#hi github repository
square = square.Square()
white = [255, 255, 255]
coordinates = square.square_coordinates

screen = pygame.display.set_mode((400, 800))
screen.fill(white)
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()

square_red_surfaces = pygame.image.load('graphics/red.png').convert_alpha()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # display squares if exist in coordinate
    for y in range(1, 10):
        for x in range(1, 20):
            square_red_rect = square_red_surfaces.get_rect(topleft=(coordinates[x], coordinates[y]))
            screen.blit


    pygame.display.update()
