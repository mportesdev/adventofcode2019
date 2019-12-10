from intcode_computer import execute_program

if __name__ == '__main__':
    with open('puzzle_5_input') as f:
        initial_memory = [int(elem) for elem in f.read().split(',')]

    # Part 1
    outputs = execute_program(initial_memory.copy(), [1])
    print(list(outputs))

    # Part 2
    outputs = execute_program(initial_memory.copy(), [5])
    print(list(outputs))
