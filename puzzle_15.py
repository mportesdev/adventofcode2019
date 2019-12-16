from intcode_computer import execute_program


class Droid:
    move_vectors = {1: (0, -1),
                    2: (0, 1),
                    3: (-1, 0),
                    4: (1, 0)}

    def __init__(self, memory, grid_size):
        self.grid = [[0] * grid_size for __ in range(grid_size)]
        self.x = grid_size // 2
        self.y = grid_size // 2
        # mark starting position in the maze
        self.grid[self.y][self.x] = 4

        self.input_buffer = []
        self.program = execute_program(memory, self.input_buffer)
        self.max_depth = 0
        self.oxygen_found = False
        self.path_to_oxygen = []

    def get_tile(self, direction):
        dx, dy = self.move_vectors[direction]
        return self.grid[self.y + dy][self.x + dx]

    def move(self, direction):
        dx, dy = self.move_vectors[direction]
        self.x += dx
        self.y += dy

    def move_opposite(self, direction):
        dx, dy = self.move_vectors[direction]
        self.x -= dx
        self.y -= dy

    def clear_maze(self):
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                if value == 1:
                    self.grid[y][x] = 0

    def explore(self, depth=0):
        if depth > self.max_depth:
            self.max_depth = depth

        for direction in (1, 4, 2, 3):
            if self.get_tile(direction) > 0:
                continue

            self.input_buffer.append(direction)
            status = next(self.program)

            if status == 0:
                # mark tile as wall
                dx, dy = self.move_vectors[direction]
                self.grid[self.y + dy][self.x + dx] = 2
            else:
                # move
                self.move(direction)
                if not self.oxygen_found:
                    self.path_to_oxygen.append(direction)

                if status == 2:
                    self.grid[self.y][self.x] = 3
                    self.oxygen_found = True
                else:
                    self.grid[self.y][self.x] = 1

                self.explore(depth=depth + 1)

                # step back
                self.input_buffer.append({1: 2, 2: 1, 3: 4, 4: 3}[direction])
                next(self.program)
                self.move_opposite(direction)
                if not self.oxygen_found:
                    assert self.path_to_oxygen.pop() == direction


if __name__ == '__main__':
    with open('puzzle_15_input') as f:
        memory = [int(elem) for elem in f.read().split(',')]

    # Part 1: map the maze and record the path to the Oxygen System
    droid = Droid(memory.copy(), grid_size=44)
    droid.explore()

    print(f'Solution: {len(droid.path_to_oxygen)}')

    # Part 2: go to the oxygen system again
    droid.input_buffer.extend(droid.path_to_oxygen)

    for direction in droid.path_to_oxygen:
        next(droid.program)
        droid.move(direction)

    # clear footprints and start as if mapping again
    droid.clear_maze()
    droid.max_depth = 0
    droid.explore()

    print(f'Solution: {droid.max_depth}')
