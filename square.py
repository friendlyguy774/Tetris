from random import randint


class Square:
    def __init__(self):
        # 3 lines to initiate shapes and 17 lines for display
        self.square_coordinates = \
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
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

        self.square_rect = \
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
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.tetris = 1

        self.moving_block1 = []
        self.moving_block2 = []
        self.moving_block3 = []
        self.moving_block4 = []

        self.store_block1 = []
        self.store_block2 = []
        self.store_block3 = []
        self.store_block4 = []

        self.block_generator = True

        self.pause = 1

        self.change = 1

    def moving_block(self):
        #  generate a random tetris depending on number(1,7)
        if self.block_generator:
            self.block_generate()
            self.block_generator = False

        self.render_block()  # render block
        if self.pause == 120:  # wait 2 second

            self.store_block()  # store old coordinate into memory
            self.block_down()  # make new coordinate
            print(self.moving_block_1)
            print(self.store_block1)
            self.delete_previous_block()  # delete old blocks
            self.pause = 0  # render new blocks back to start of loop

        else:
            self.pause += 1


    def block_generate(self):
        if self.tetris == 1:
            self.moving_block_1 = [0, 4]
            self.moving_block_2 = [0, 5]
            self.moving_block_3 = [1, 5]
            self.moving_block_4 = [1, 6]

    # store block coordinate before moving it down
    def store_block(self):
        self.store_block1 = self.moving_block_1
        self.store_block2 = self.moving_block_2
        self.store_block3 = self.moving_block_3
        self.store_block4 = self.moving_block_4

    #  make specific coordinate 1
    def render_block(self):
        self.square_coordinates[self.moving_block_1[0]][self.moving_block_1[1]] = self.tetris
        self.square_coordinates[self.moving_block_2[0]][self.moving_block_2[1]] = self.tetris
        self.square_coordinates[self.moving_block_3[0]][self.moving_block_3[1]] = self.tetris
        self.square_coordinates[self.moving_block_4[0]][self.moving_block_4[1]] = self.tetris

    # new coordinate is below by one
    def block_down(self):
        self.moving_block_1[0] = self.moving_block_1[0] + 1
        self.moving_block_2[0] = self.moving_block_2[0] + 1
        self.moving_block_3[0] = self.moving_block_3[0] + 1
        self.moving_block_4[0] = self.moving_block_4[0] + 1

    # delete the block
    def delete_previous_block(self):
        self.square_coordinates[self.store_block1[0]][self.store_block1[1]] = 0
        self.square_coordinates[self.store_block2[0]][self.store_block2[1]] = 0
        self.square_coordinates[self.store_block3[0]][self.store_block3[1]] = 0
        self.square_coordinates[self.store_block4[0]][self.store_block4[1]] = 0
