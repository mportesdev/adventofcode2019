from itertools import permutations, cycle

from intcode_computer import execute_program


def get_output_signal(memory, phases):
    value = 0
    for phase in phases:
        value = next(execute_program([list(memory), 0], [phase, value]))
    return value


def run_feedback_loop(memory, phases):
    states = [[list(memory), 0] for __ in range(5)]
    input_buffers = [[] for __ in range(5)]
    value = 0
    init_phase = True

    for amp in cycle(range(5)):
        if init_phase:
            input_buffers[amp].extend([phases[amp], value])
        else:
            input_buffers[amp].append(value)

        if amp == 4:
            init_phase = False

        try:
            value = next(execute_program(states[amp], input_buffers[amp]))
        except StopIteration:
            return value


if __name__ == '__main__':
    with open('puzzle_7_input') as f:
        memory = tuple(int(elem) for elem in f.read().split(','))

    # Part 1
    solution = max(get_output_signal(memory, phases)
                   for phases in permutations(range(5), 5))
    print(f'Solution: {solution}')

    # Part 2
    solution = max(run_feedback_loop(memory, phases)
                   for phases in permutations(range(5, 10), 5))
    print(f'Solution: {solution}')
