from pathlib import Path

from intcode_computer import execute_program


def save_grid(frame_number: int, score: int, grid: list) -> None:
    """Save animation frame as a text file to be used by the script
       img/puzzle_13_animation.py
    """
    temp_path = Path('img/tmp')
    if not temp_path.exists():
        temp_path.mkdir()

    with (temp_path / f'{frame_number:04}.txt').open('w', encoding='utf-8') as f:
        f.write(f'{score}\n')
        for line in (''.join(' *#=o'[n] for n in row) for row in grid):
            f.write(f'{line}\n')


def play_game(grid: list, memory: list) -> int:
    input_buffer = [0]
    game_program = execute_program(memory, input_buffer)
    score = 0
    paddle_x = None
    ball_x = None
    frame = 0

    while True:
        try:
            x = next(game_program)
            y = next(game_program)
            id = next(game_program)
        except StopIteration:
            break

        if x == -1 and y == 0:
            score = id
            continue

        grid[y][x] = id

        if id == 3:
            paddle_x = x

        if id == 4:
            if x != ball_x and ball_x:
                # execute when the ball moved, but not when it is being
                # drawn for the first time
                if paddle_x < x:
                    input_buffer.append(1)
                elif paddle_x > x:
                    input_buffer.append(-1)
                else:
                    input_buffer.append(0)

                save_grid(frame, score, grid)
                frame += 1

            ball_x = x

    # save the winning screen
    save_grid(frame, score, grid)
    return score


if __name__ == '__main__':
    with open('puzzle_13_input') as f:
        memory = [int(elem) for elem in f.read().split(',')]

    # Part 1
    grid = [[0] * 38 for __ in range(21)]
    play_game(grid, memory.copy())
    print(f'Solution: {sum(row.count(2) for row in grid)}')

    # Part 2
    grid = [[0] * 38 for __ in range(21)]
    game_memory = memory.copy()

    # insert coins
    game_memory[0] = 2

    final_score = play_game(grid, game_memory)
    print(f'Solution: {final_score}')
