from itertools import product

from intcode_computer import execute_program

if __name__ == '__main__':
    # Part 1
    with open('puzzle_2_input') as f:
        memory = [int(elem) for elem in f.read().split(',')]

    memory[1:3] = [12, 2]
    __ = list(execute_program(memory, []))
    print(f'Solution: {memory[0]}')

    # Part 2
    with open('puzzle_2_input') as f:
        initial_state = [int(elem) for elem in f.read().split(',')]

    # brute force search for the desired output of 19690720
    for noun, verb in product(range(100), range(100)):
        memory = initial_state[:]
        memory[1:3] = [noun, verb]
        __ = list(execute_program(memory, []))
        if memory[0] == 19690720:
            print(f'Solution: {100*noun + verb}')
            break
