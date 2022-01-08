import pygame
from sys import exit


# scan all coordinates for blocks
# if blocks exist, print out the box depending on colour
def square_printing():
    for y in range(0, 20):
        for x in range(0, 10):
            if square_coordinates[y][x] == 1:
                square_rect[y][x] = (square_red_surfaces.get_rect(topleft=(40 * x, 40 * y)))
                screen.blit(square_red_surfaces, square_rect[y][x])
            if square_coordinates[y][x] == 2:
                square_rect[y][x] = (square_green_surfaces.get_rect(topleft=(40 * x, 40 * y)))
                screen.blit(square_green_surfaces, square_rect[y][x])
            if square_coordinates[y][x] == 3:
                square_rect[y][x] = (square_yellow_surfaces.get_rect(topleft=(40 * x, 40 * y)))
                screen.blit(square_yellow_surfaces, square_rect[y][x])
            if square_coordinates[y][x] == 4:
                square_rect[y][x] = (square_orange_surfaces.get_rect(topleft=(40 * x, 40 * y)))
                screen.blit(square_orange_surfaces, square_rect[y][x])
            if square_coordinates[y][x] == 5:
                square_rect[y][x] = (square_pink_surfaces.get_rect(topleft=(40 * x, 40 * y)))
                screen.blit(square_pink_surfaces, square_rect[y][x])
            if square_coordinates[y][x] == 6:
                square_rect[y][x] = (square_blue_surfaces.get_rect(topleft=(40 * x, 40 * y)))
                screen.blit(square_blue_surfaces, square_rect[y][x])
            if square_coordinates[y][x] == 7:
                square_rect[y][x] = (square_purple_surfaces.get_rect(topleft=(40 * x, 40 * y)))
                screen.blit(square_purple_surfaces, square_rect[y][x])


def block_generator():
    if tetris == 1:
        return [[0, 4], [0, 5], [1, 5], [1, 6]]


pygame.init()


white = [255, 255, 255]

screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()
counter = 1

square_coordinates = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 2, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 3, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                     [0, 0, 0, 0, 1, 1, 1, 1, 0, 0]
square_rect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tetris = 1
moving_block = []
store_block = []
block_generate = True

square_red_surfaces = pygame.image.load('graphics/red.png').convert_alpha()  # red for Z_blocks, 1
square_green_surfaces = pygame.image.load('graphics/green.png').convert_alpha()  # green for S_blocks, 2
square_yellow_surfaces = pygame.image.load('graphics/yellow.png').convert_alpha()  # yellow for O_blocks, 3
square_orange_surfaces = pygame.image.load('graphics/orange.png').convert_alpha()  # orange for L_blocks, 4
square_pink_surfaces = pygame.image.load('graphics/pink.png').convert_alpha()  # pink for J_blocks, 5
square_blue_surfaces = pygame.image.load('graphics/blue.png').convert_alpha()  # blue for I-blocks, 6
square_purple_surfaces = pygame.image.load('graphics/purple.png').convert_alpha()  # purple for T_blocks, 7


def move_down(mb):
    store = mb
    for j in range(4):
        mb[j][0] += 1
    return store, mb


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # generate a tetris
    if block_generate:
        moving_block = block_generator()
        for i in range(4):
            square_coordinates[moving_block[i][0]][moving_block[i][1]] = tetris
        square_printing()
        block_generate = False

    if counter == 100:
        # new moving_block coordinates when block moves down are inputted and old block_coordinates are stored
        store_block, moving_block = move_down(moving_block)
        print(store_block, moving_block)
        # for all store_block values, equate them to 0 to delete them
        for i in range(4):
            square_coordinates[store_block[i][0]][store_block[i][1]] = 0
        print(square_coordinates)
        screen.fill(white)
        for i in range(4):
            square_coordinates[moving_block[i][0]][moving_block[i][1]] = tetris
        square_printing()
        counter = 1
    else: counter += 1

    pygame.display.update()
    pygame.time.Clock().tick(100)
