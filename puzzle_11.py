from intcode_computer import execute_program


class Robot:
    def __init__(self, x, y, memory):
        self.x = x
        self.y = y
        self.direction = (0, -1)
        self.input = []
        self.program = execute_program(memory, self.input)


def paint_job(grid, robot):
    turn_dispatch = {
        (0, -1): {0: (-1, 0), 1: (1, 0)},        # up    ->  left | right
        (1, 0): {0: (0, -1), 1: (0, 1)},         # right ->    up | down
        (0, 1): {0: (1, 0), 1: (-1, 0)},         # down  -> right | left
        (-1, 0): {0: (0, 1), 1: (0, -1)},        # left  ->  down | up
    }

    while True:
        current_color = grid[robot.y][robot.x] & 1
        robot.input.append(current_color)

        try:
            color_to_paint = next(robot.program)
        except StopIteration:
            break
        else:
            assert color_to_paint in (0, 1)
            # paint current tile
            grid[robot.y][robot.x] = color_to_paint

        turn = next(robot.program)
        assert turn in (0, 1)
        # turn robot
        robot.direction = turn_dispatch[robot.direction][turn]
        # move robot
        robot.x += robot.direction[0]
        robot.y += robot.direction[1]

    return sum(n < 2 for row in grid for n in row)


if __name__ == '__main__':
    with open('puzzle_11_input') as f:
        memory = [int(elem) for elem in f.read().split(',')]

    # Part 1
    grid = [[2] * 120 for __ in range(80)]
    robot = Robot(90, 70, memory.copy())
    print(f'Solution: {paint_job(grid, robot)}')

    # Part 2
    grid = [[2] * 80 for __ in range(60)]
    robot = Robot(10, 10, memory.copy())
    # starting tile must be white
    grid[robot.y][robot.x] = 1
    paint_job(grid, robot)

    print('Solution:')
    print('\n'.join(''.join(' █-'[n] for n in row)
                    for row in grid if 0 in row or 1 in row))
