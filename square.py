class Square:
    def __init__(self):
        # 3 lines to initiate shapes and 17 lines for display
        self.block_generate = None
        self.square_coordinates = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.square_rect = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 1, 1, 1, 1, 0, 0]]

        self.stationary = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.tetris = 7
        self.moving_block = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.store_block = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.block_generate = True
        self.touch_floor = False
        self.lose = False
        self.move_down = True
        self.rotation_counter = 1

    def update_moving_block(self):

        temporary_storage = [0, 0, 0, 0]

        for a in range(4):
            temporary_storage[a] = [x for x in self.moving_block[a]]

        for y in temporary_storage:
            y[0] += 1

        for z in temporary_storage:
            if z[0] < 20:
                if self.stationary[z[0]][z[1]]:
                    self.move_down = False
                    self.touch_floor = True
            if z[0] == 20:
                self.move_down = False
                self.touch_floor = True

        if self.move_down:
            self.temporary_store()
            self.block_down()
            self.delete_old_tetris()
            self.render_new_tetris()
        print(self.square_coordinates)

    def generate_block(self):
        if self.block_generate:
            # choose a random number
            # 1 -> z, 2 -> s, 3 -> 0, 4 -> l, 5 -> j, 6 -> i, 7 -> t
            self.rotation_counter = 1
            if self.tetris == 1:
                self.moving_block = [[0, 4], [0, 5], [1, 5], [1, 6]]
            if self.tetris == 2:
                self.moving_block = [[1, 4], [1, 5], [0, 5], [0, 6]]
            if self.tetris == 3:
                self.moving_block = [[0, 5], [0, 6], [1, 5], [1, 6]]
            if self.tetris == 4:
                self.moving_block = [[0, 5], [1, 5], [2, 5], [2, 6]]
            if self.tetris == 5:
                self.moving_block = [[2, 5], [2, 6], [1, 6], [0, 6]]
            if self.tetris == 6:
                self.moving_block = [[0, 4], [0, 5], [0, 6], [0, 7]]
            if self.tetris == 7:
                self.moving_block = [[0, 4], [0, 5], [0, 6], [1, 5]]
            self.block_generate = False
            self.move_down = True
            for x in self.moving_block:
                self.square_coordinates[x[0]][x[1]] = self.tetris
        for x in self.moving_block:
            if self.stationary[x[0]][x[1]]:
                self.lose = True

    def temporary_store(self):
        for z in range(4):
            self.store_block[z] = [j for j in self.moving_block[z]]

    def block_down(self):

        for x in self.moving_block:
            x[0] += 1

    def touch_down(self):
        if self.touch_floor:
            for x in self.moving_block:
                self.square_coordinates[x[0]][x[1]] = self.tetris
                self.stationary[x[0]][x[1]] = 1
                self.block_generate = True
                self.touch_floor = False

    def delete_old_tetris(self):
        for x in self.store_block:
            self.square_coordinates[x[0]][x[1]] = 0

    def render_new_tetris(self):
        for y in self.moving_block:
            self.square_coordinates[y[0]][y[1]] = self.tetris

    def move_block_left(self):
        # create a temporary block that moved left
        # check if touch side
        # check if touch stationary
        # if never touch side or touch stationary, able to move left
        # store in temporary store
        # move the block left
        # delete before block
        # paste the new block

        created_temporary_block = [0, 0, 0, 0]
        move_left = True
        for a in range(4):
            created_temporary_block[a] = [b for b in self.moving_block[a]]

        for c in created_temporary_block:
            c[1] -= 1

        for z in created_temporary_block:
            if self.stationary[z[0]][z[1]] or z[1] < 0:
                move_left = False

        if move_left:
            self.temporary_store()

            for x in self.moving_block:
                x[1] -= 1

            self.delete_old_tetris()

            self.render_new_tetris()

    def move_block_right(self):
        # create a temporary block that moved left
        # check if touch side
        # check if touch stationary
        # if never touch side or touch stationary, able to move left
        # store in temporary store
        # move the block left
        # delete before block
        # paste the new block

        created_temporary_block = [0, 0, 0, 0]
        move_right = True
        for a in range(4):
            created_temporary_block[a] = [b for b in self.moving_block[a]]

        for c in created_temporary_block:
            c[1] += 1

        for z in created_temporary_block:
            if z[1] < 9:
                if self.stationary[z[0]][z[1]]:
                    move_right = False
            if z[1] == 10:
                move_right = False

        if move_right:
            self.temporary_store()

            for x in self.moving_block:
                x[1] += 1

            self.delete_old_tetris()

            self.render_new_tetris()

    def move_block_down(self):
        # create a temporary block that moved left
        # check if touch side
        # check if touch stationary
        # if never touch side or touch stationary, able to move left
        # store in temporary store
        # move the block left
        # delete before block
        # paste the new block

        created_temporary_block = [0, 0, 0, 0]
        move_down = True
        for a in range(4):
            created_temporary_block[a] = [b for b in self.moving_block[a]]

        for c in created_temporary_block:
            c[0] += 1

        for z in created_temporary_block:
            if z[0] < 20:
                if self.stationary[z[0]][z[1]]:
                    move_down = False
            if z[0] == 20:
                move_down = False

        if move_down:
            self.temporary_store()

            for x in self.moving_block:
                x[0] += 1

            self.delete_old_tetris()

            self.render_new_tetris()

    def update_rotating_block_clockwise(self):
        self.temporary_store()
        self.rotate_block_clockwise()
        self.delete_old_tetris()
        self.render_new_tetris()

    def rotate_block_clockwise(self):

        [[Ya, Xa], [Yb, Xb], [Yc, Xc], [Yd, Xd]] = self.moving_block
        rotation = True

        if self.tetris == 1:
            if self.rotation_counter == 1 and rotation:
                self.moving_block = [[Ya + 2, Xa], [Yb + 1, Xb - 1], [Yc, Xc], [Yd - 1, Xd - 1]]
                self.rotation_counter = 2
                rotation = False

            if self.rotation_counter == 2 and rotation:
                self.moving_block = [[Ya, Xa + 2], [Yb + 1, Xb + 1], [Yc, Xc], [Yd + 1, Xd - 1]]
                self.rotation_counter = 3
                rotation = False

            if self.rotation_counter == 3 and rotation:
                self.moving_block = [[Ya - 2, Xa], [Yb - 1, Xb + 1], [Yc, Xc], [Yd + 1, Xd + 1]]
                self.rotation_counter = 4
                rotation = False

            if self.rotation_counter == 4 and rotation:
                self.moving_block = [[Ya, Xa - 2], [Yb - 1, Xb - 1], [Yc, Xc], [Yd - 1, Xd + 1]]
                self.rotation_counter = 1
                rotation = False

        if self.tetris == 2:
            if self.rotation_counter == 1 and rotation:
                self.moving_block = [[Ya + 1, Xa + 1], [Yb, Xb], [Yc + 1, Xc - 1], [Yd, Xd - 2]]
                self.rotation_counter = 2
                rotation = False

            if self.rotation_counter == 2 and rotation:
                self.moving_block = [[Ya - 1, Xa + 1], [Yb, Xb], [Yc + 1, Xc + 1], [Yd + 2, Xd]]
                self.rotation_counter = 3
                rotation = False

            if self.rotation_counter == 3 and rotation:
                self.moving_block = [[Ya - 1, Xa - 1], [Yb, Xb], [Yc - 1, Xc + 1], [Yd, Xd + 2]]
                self.rotation_counter = 4
                rotation = False

            if self.rotation_counter == 4 and rotation:
                self.moving_block = [[Ya + 1, Xa - 1], [Yb, Xb], [Yc - 1, Xc - 1], [Yd - 2, Xd]]
                self.rotation_counter = 1
                rotation = False

        if self.tetris == 4:
            if self.rotation_counter == 1 and rotation:
                self.moving_block = [[Ya + 2, Xa], [Yb + 1, Xb + 1], [Yc, Xc + 2], [Yd - 1, Xd + 1]]
                self.rotation_counter = 2
                rotation = False

            if self.rotation_counter == 2 and rotation:
                self.moving_block = [[Ya, Xa + 2], [Yb - 1, Xb + 1], [Yc - 2, Xc], [Yd - 1, Xd - 1]]
                self.rotation_counter = 3
                rotation = False

            if self.rotation_counter == 3 and rotation:
                self.moving_block = [[Ya - 2, Xa], [Yb - 1, Xb - 1], [Yc, Xc - 2], [Yd + 1, Xd - 1]]
                self.rotation_counter = 4
                rotation = False

            if self.rotation_counter == 4 and rotation:
                self.moving_block = [[Ya, Xa - 2], [Yb + 1, Xb - 1], [Yc + 2, Xc], [Yd + 1, Xd + 1]]
                self.rotation_counter = 1
                rotation = False

        if self.tetris == 5:
            if self.rotation_counter == 1 and rotation:
                self.moving_block = [[Ya - 1, Xa + 1], [Yb - 2, Xb], [Yc - 1, Xc - 1], [Yd, Xd - 2]]
                self.rotation_counter = 2
                rotation = False

            if self.rotation_counter == 2 and rotation:
                self.moving_block = [[Ya - 1, Xa - 1], [Yb, Xb - 2], [Yc + 1, Xc - 1], [Yd + 2, Xd]]
                self.rotation_counter = 3
                rotation = False

            if self.rotation_counter == 3 and rotation:
                self.moving_block = [[Ya + 1, Xa - 1], [Yb + 2, Xb], [Yc + 1, Xc + 1], [Yd, Xd + 2]]
                self.rotation_counter = 4
                rotation = False

            if self.rotation_counter == 4 and rotation:
                self.moving_block = [[Ya + 1, Xa + 1], [Yb, Xb + 2], [Yc - 1, Xc + 1], [Yd - 2, Xd]]
                self.rotation_counter = 1
                rotation = False

        if self.tetris == 6:
            if self.rotation_counter == 1 and rotation:
                self.moving_block = [[Ya + 2, Xa + 1], [Yb + 1, Xb], [Yc, Xc - 1], [Yd - 1, Xd - 2]]
                self.rotation_counter = 2
                rotation = False

            if self.rotation_counter == 2 and rotation:
                self.moving_block = [[Ya - 1, Xa + 2], [Yb, Xb + 1], [Yc + 1, Xc], [Yd + 2, Xd - 1]]
                self.rotation_counter = 3
                rotation = False

            if self.rotation_counter == 3 and rotation:
                self.moving_block = [[Ya - 2, Xa - 1], [Yb - 1, Xb], [Yc, Xc + 1], [Yd + 1, Xd + 2]]
                self.rotation_counter = 4
                rotation = False

            if self.rotation_counter == 4 and rotation:
                self.moving_block = [[Ya + 1, Xa - 2], [Yb, Xb - 1], [Yc - 1, Xc], [Yd - 2, Xd + 1]]
                self.rotation_counter = 1
                rotation = False

        if self.tetris == 7:
            if self.rotation_counter == 1 and rotation:
                self.moving_block = [[Ya + 1, Xa + 1], [Yb, Xb], [Yc - 1, Xc - 1], [Yd - 1, Xd + 1]]
                self.rotation_counter = 2
                rotation = False

            if self.rotation_counter == 2 and rotation:
                self.moving_block = [[Ya - 1, Xa + 1], [Yb, Xb], [Yc + 1, Xc - 1], [Yd - 1, Xd - 1]]
                self.rotation_counter = 3
                rotation = False

            if self.rotation_counter == 3 and rotation:
                self.moving_block = [[Ya - 1, Xa - 1], [Yb, Xb], [Yc + 1, Xc + 1], [Yd + 1, Xd - 1]]
                self.rotation_counter = 4
                rotation = False

            if self.rotation_counter == 4 and rotation:
                self.moving_block = [[Ya + 1, Xa - 1], [Yb, Xb], [Yc - 1, Xc + 1], [Yd + 1, Xd + 1]]
                self.rotation_counter = 1
                rotation = False

