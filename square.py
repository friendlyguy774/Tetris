import random


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
                                   [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                                   [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                                   [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

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
                           [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.tetris = 6
        self.moving_block = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.store_block = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.block_generate = True
        self.touch_floor = False
        self.lose = False
        self.move_down = True
        self.rotation_counter = 1
        self.check_right = False
        self.check_left = False
        self.check_up = False
        self.check_ceiling = False
        self.touching_stationary = False
        self.prime_line = 20
        self.prime_line_exist = True

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
            self.tetris = (random.randint(1, 7))
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
            self.update_rotating_block_clockwise()  # delete in future
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

        self.temporary_store()

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

        # if rotated block touch ceiling by 1,move it down by 1
        # if rotated block touch left wall by 1, move it to the left by 1
        # if rotated block touch right wall by 1, move it to the right by 1
        # if rotated block touch the floor by 1, move it up by 1
        # interaction of rotated block with stationary
        # order of check
        # 1. check if can move left
        # 2. check if can move right
        # 3. check if can move up

        self.check_if_touch_ceiling()
        self.check_if_touch_left()
        self.check_if_touch_right()
        self.check_if_touch_floor()
        self.check_if_touch_stationary()

    def check_if_touch_ceiling(self):

        touch_ceiling_by_1 = False
        touch_ceiling_by_2 = False

        for y in self.moving_block:
            if y[0] < 0:
                touch_ceiling_by_1 = True
            if y[0] < -1:
                touch_ceiling_by_2 = True

        if touch_ceiling_by_1:
            for y in self.moving_block:
                y[0] += 1
        if touch_ceiling_by_2:
            for y in self.moving_block:
                y[0] += 1

    def check_if_touch_left(self):

        touch_left_by_1 = False
        touch_left_by_2 = False

        for x in self.moving_block:
            if x[1] < 0:
                touch_left_by_1 = True
            if x[1] < -1:
                touch_left_by_2 = True

        if touch_left_by_1:
            for x in self.moving_block:
                x[1] += 1

        if touch_left_by_2:
            for x in self.moving_block:
                x[1] += 1

    def check_if_touch_right(self):

        touch_right_by_1 = False
        touch_right_by_2 = False

        for x in self.moving_block:
            if x[1] > 9:
                touch_right_by_1 = True
            if x[1] > 10:
                touch_right_by_2 = True

        if touch_right_by_1:
            for x in self.moving_block:
                x[1] -= 1
        if touch_right_by_2:
            for x in self.moving_block:
                x[1] -= 1

    def check_if_touch_floor(self):

        touch_floor_by_1 = False
        touch_floor_by_2 = False

        for y in self.moving_block:
            if y[0] > 19:
                touch_floor_by_1 = True
            if y[0] > 20:
                touch_floor_by_2 = True

        if touch_floor_by_1:
            for y in self.moving_block:
                y[0] -= 1

        if touch_floor_by_2:
            for y in self.moving_block:
                y[0] -= 1

    def check_if_touch_stationary(self):
        # check if moving block right will cause it not to touch stationary
        # if no, return to original value
        # check if moving block left will cause it not to touch stationary
        # if no, return to original value
        # check if moving block up will cause it not to touch stationary and ceiling
        # if never touch stationary and ceiling, modify it
        # if never touch stationary and touch ceiling, return it to normal value

        for block in self.moving_block:
            if self.stationary[block[0]][block[1]]:
                self.check_right = True
                self.touching_stationary = True

        while self.touching_stationary:
            if self.check_right:
                self.temporary_right()
                print(self.check_right)

            if self.check_left:
                self.temporary_left()
                print(self.check_left)

            if self.check_up:
                self.temporary_up()
                print(self.check_up)

            if self.check_ceiling:

                for y in range(4):
                    self.moving_block[y] = [k for k in self.store_block[y]]

                self.check_ceiling = False

    def temporary_right(self):

        temporary_storage = [[0, 0], [0, 0], [0, 0], [0, 0]]
        cannot_move_right = False
        check_right_again = True
        move_right_again = False

        for x in range(4):
            temporary_storage[x] = [j for j in self.moving_block[x]]

        for block in self.moving_block:
            block[1] += 1

        if self.tetris == 6:
            for block in self.moving_block:
                if block[1] <= 9:
                    if self.stationary[block[0]][block[1]]:
                        check_right_again = True
                        move_right_again = True
                        print("touching stationary")
                    else:
                        self.touching_stationary = False
                        print("not touching stationary")

        if move_right_again:
            for block in self.moving_block:
                block[1] += 1

        if check_right_again:
            for block in self.moving_block:
                if block[1] <= 9:
                    if self.stationary[block[0]][block[1]]:
                        cannot_move_right = True
                    else:
                        self.touching_stationary = False
                if block[1] > 9:
                    cannot_move_right = True

        if cannot_move_right:
            for y in range(4):
                self.moving_block[y] = [k for k in temporary_storage[y]]  # return coordinates to its normal value
                self.check_left = True

        self.check_right = False

    def temporary_left(self):

        temporary_storage = [0, 0, 0, 0]
        cannot_move_left = False
        check_left_again = True
        move_left_again = False

        for x in range(4):
            temporary_storage[x] = [j for j in self.moving_block[x]]

        for block in self.moving_block:
            block[1] -= 1

        if self.tetris == 6:
            for block in self.moving_block:
                if block[1] >= 0:
                    if self.stationary[block[0]][block[1]]:
                        check_left_again = True
                        move_left_again = True
                    else:
                        self.touching_stationary = False

        if move_left_again:
            for block in self.moving_block:
                block[1] -= 1

        if check_left_again:
            for block in self.moving_block:
                if block[1] >= 0:
                    if self.stationary[block[0]][block[1]]:
                        cannot_move_left = True
                    else:
                        self.touching_stationary = False
                if block[1] < 0:
                    cannot_move_left = True

        if cannot_move_left:
            for y in range(4):
                self.moving_block[y] = [k for k in temporary_storage[y]]  # return coordinates to its normal value
                self.check_up = True

        self.check_left = False

    def temporary_up(self):

        temporary_storage = [0, 0, 0, 0]
        block_is_still_touching_stationary = False
        block_is_touching_ceiling = False

        for block in self.moving_block:
            block[0] -= 1
            print(self.stationary[block[0]][block[1]])

        for block in self.moving_block:
            if self.stationary[block[0]][block[1]]:
                block_is_still_touching_stationary = True
            if block[0] < 0:
                block_is_touching_ceiling = True

        if block_is_still_touching_stationary:
            self.check_right = True
            self.touching_stationary = True
        else:
            self.touching_stationary = False

        if block_is_touching_ceiling:
            self.check_ceiling = True
            self.check_right = False
            self.touching_stationary = False

        self.check_up = False

    def clear_stationary_blocks(self):

        # check every line of square.stationary if equals to 1

        # if in the line of square.stationary (prime line) has all coordinates equal to 1:
        # paste the square.stationary for line below the prime line into square.temporary_stationary_coordinate
        # paste the square.coordinate for line below the prime line into square.temporary_coordinate
        # equate coordinates for square.stationary for prime line to 0
        # equate coordinates for square.coordinate for prime line to 0
        # move coordinates of square.stationary for line above prime line down
        # move coordinates of square.coordinate for line above prime line down

        # run check again on every line of square.stationary if equals to 1
        self.check_for_prime_line()
        while self.prime_line_exist:
            self.delete_prime_line()
            self.move_list_above_down()
            self.check_for_prime_line()
            self.print_coordinates()

    def check_for_prime_line(self):
        line_is_prime = True
        prime_check = []

        for y in range(20):
            line_is_prime = all(self.stationary[y])
            prime_check.append(line_is_prime)
            if line_is_prime:
                self.prime_line = y

        if any(prime_check):
            self.prime_line_exist = True
        else:
            self.prime_line_exist = False

    def delete_prime_line(self):
        for element in range(10):
            self.square_coordinates[self.prime_line][element] = 0
            self.stationary[self.prime_line][element] = 0

    def move_list_above_down(self):
        touch_ceiling = False
        line_pasted_to = self.prime_line
        line_cut_from = line_pasted_to - 1

        while not touch_ceiling:

            self.square_coordinates[line_pasted_to] = [x for x in self.square_coordinates[line_cut_from]]
            self.stationary[line_pasted_to] = [x for x in self.stationary[line_cut_from]]

            line_pasted_to -= 1
            line_cut_from -= 1

            if line_pasted_to == 0:
                touch_ceiling = True
                for element in range(10):
                    self.square_coordinates[0][element] = 0
                    self.stationary[0][element] = 0

    def print_coordinates(self):
        for y in self.square_coordinates:
            print(y)
        print("\n")
        for x in self.stationary:
            print(x)
        print("\n")
