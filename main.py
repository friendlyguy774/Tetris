import pygame
from pygame import K_LEFT, K_RIGHT, K_DOWN, K_d

import square
from sys import exit


# scan all coordinates for blocks
# if blocks exist, print out the box depending on colour
def square_printing():
    for y in range(20):
        for x in range(10):
            if square.square_coordinates[y][x] == 1:
                square.square_rect[y][x] = (square_red_surfaces.get_rect(topleft=(40 * x, 40 * y)))
                screen.blit(square_red_surfaces, square.square_rect[y][x])
            if square.square_coordinates[y][x] == 2:
                square.square_rect[y][x] = (square_green_surfaces.get_rect(topleft=(40 * x, 40 * y)))
                screen.blit(square_green_surfaces, square.square_rect[y][x])
            if square.square_coordinates[y][x] == 3:
                square.square_rect[y][x] = (square_yellow_surfaces.get_rect(topleft=(40 * x, 40 * y)))
                screen.blit(square_yellow_surfaces, square.square_rect[y][x])
            if square.square_coordinates[y][x] == 4:
                square.square_rect[y][x] = (square_orange_surfaces.get_rect(topleft=(40 * x, 40 * y)))
                screen.blit(square_orange_surfaces, square.square_rect[y][x])
            if square.square_coordinates[y][x] == 5:
                square.square_rect[y][x] = (square_pink_surfaces.get_rect(topleft=(40 * x, 40 * y)))
                screen.blit(square_pink_surfaces, square.square_rect[y][x])
            if square.square_coordinates[y][x] == 6:
                square.square_rect[y][x] = (square_blue_surfaces.get_rect(topleft=(40 * x, 40 * y)))
                screen.blit(square_blue_surfaces, square.square_rect[y][x])
            if square.square_coordinates[y][x] == 7:
                square.square_rect[y][x] = (square_purple_surfaces.get_rect(topleft=(40 * x, 40 * y)))
                screen.blit(square_purple_surfaces, square.square_rect[y][x])


pygame.init()

white = [255, 255, 255]

screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()
counter = 0
game_running = True

square = square.Square()

square_red_surfaces = pygame.image.load('graphics/red.png').convert_alpha()  # red for Z_blocks, 1
square_green_surfaces = pygame.image.load('graphics/green.png').convert_alpha()  # green for S_blocks, 2
square_yellow_surfaces = pygame.image.load('graphics/yellow.png').convert_alpha()  # yellow for O_blocks, 3
square_orange_surfaces = pygame.image.load('graphics/orange.png').convert_alpha()  # orange for L_blocks, 4
square_pink_surfaces = pygame.image.load('graphics/pink.png').convert_alpha()  # pink for J_blocks, 5
square_blue_surfaces = pygame.image.load('graphics/blue.png').convert_alpha()  # blue for I-blocks, 6
square_purple_surfaces = pygame.image.load('graphics/purple.png').convert_alpha()  # purple for T_blocks, 7

# flow of the game
# generate block
# scan if block that is generated is already filled, if so then lose game
# scan if bottom is filled or is beyond the game (y-axis >19), if so leave the block there and generate_block
# move block down

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                square.move_block_left()
            if event.key == K_RIGHT:
                square.move_block_right()
            if event.key == K_DOWN:
                square.move_block_down()

        if event.type == pygame.KEYUP:
            if event.key == K_d:
                square.update_rotating_block_clockwise()

    if game_running:
        screen.fill(white)

        if square.lose:
            game_running = False
            break

        square.generate_block()
        square_printing()

        if counter == 60:
            square.update_moving_block()
            counter = 1
        else:
            counter += 1
        square.touch_down()

    pygame.display.update()
    pygame.time.Clock().tick(100)
