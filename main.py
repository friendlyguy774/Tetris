import pygame
import square
from sys import exit

pygame.init()

square = square.Square()
white = [255, 255, 255]
coordinates = square.square_coordinates

screen = pygame.display.set_mode((400, 800))
screen.fill(white)
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()

square_red_surfaces = pygame.image.load('graphics/red.png').convert_alpha()  # red for Z_blocks, 1
square_green_surfaces = pygame.image.load('graphics/green.png').convert_alpha()  # green for S_blocks, 2
square_yellow_surfaces = pygame.image.load('graphics/yellow.png').convert_alpha()  # yellow for O_blocks, 3
square_orange_surfaces = pygame.image.load('graphics/orange.png').convert_alpha()  # orange for L_blocks, 4
square_pink_surfaces = pygame.image.load('graphics/pink.png').convert_alpha()  # pink for J_blocks, 5
square_blue_surfaces = pygame.image.load('graphics/blue.png').convert_alpha()  # blue for I-blocks, 6
square_purple_surfaces = pygame.image.load('graphics/purple.png').convert_alpha()  # purple for T_blocks, 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # scan all coordinates for blocks
    # if blocks exist, print out the box depending on colour
    for y in range(0, 20):
        for x in range(0, 10):
            if square.square_coordinates[y][x] == 1:
                square.square_rect[y][x] = (square_red_surfaces.get_rect(topleft = (40*x, 40*y)))
                screen.blit(square_red_surfaces, square.square_rect[y][x])
            if square.square_coordinates[y][x] == 2:
                square.square_rect[y][x] = (square_green_surfaces.get_rect(topleft = (40*x, 40*y)))
                screen.blit(square_green_surfaces, square.square_rect[y][x])
            if square.square_coordinates[y][x] == 3:
                square.square_rect[y][x] = (square_yellow_surfaces.get_rect(topleft = (40*x, 40*y)))
                screen.blit(square_yellow_surfaces, square.square_rect[y][x])
            if square.square_coordinates[y][x] == 4:
                square.square_rect[y][x] = (square_orange_surfaces.get_rect(topleft = (40*x, 40*y)))
                screen.blit(square_orange_surfaces, square.square_rect[y][x])
            if square.square_coordinates[y][x] == 5:
                square.square_rect[y][x] = (square_pink_surfaces.get_rect(topleft = (40*x, 40*y)))
                screen.blit(square_pink_surfaces, square.square_rect[y][x])
            if square.square_coordinates[y][x] == 6:
                square.square_rect[y][x] = (square_blue_surfaces.get_rect(topleft = (40*x, 40*y)))
                screen.blit(square_blue_surfaces, square.square_rect[y][x])
            if square.square_coordinates[y][x] == 7:
                square.square_rect[y][x] = (square_purple_surfaces.get_rect(topleft = (40*x, 40*y)))
                screen.blit(square_purple_surfaces, square.square_rect[y][x])

    pygame.display.update()
