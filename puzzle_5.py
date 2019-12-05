def decimal_digit(n, order):
    return (n // 10**order) % 10


def execute_program(memory, inputs):
    """Run the Intcode program, modifying the memory in-place."""
    # instruction pointer
    ip = 0
    input_buffer = iter(inputs)

    dispatch_dict = {1: lambda x, y: x + y,
                     2: lambda x, y: x * y,
                     7: lambda x, y: 1 if x < y else 0,
                     8: lambda x, y: 1 if x == y else 0}

    while (opcode := memory[ip]) != 99:
        param_1_mode = 'immediate' if decimal_digit(opcode, 2) else 'position'
        param_2_mode = 'immediate' if decimal_digit(opcode, 3) else 'position'
        opcode = opcode % 100

        if opcode in (1, 2, 7, 8):
            param_1, param_2, target_addr = memory[ip + 1:ip + 4]
            if param_1_mode == 'position':
                param_1 = memory[param_1]
            if param_2_mode == 'position':
                param_2 = memory[param_2]

            memory[target_addr] = dispatch_dict[opcode](param_1, param_2)
            ip += 4

        elif opcode in (3, 4):
            param = memory[ip + 1]
            if opcode == 3:
                memory[param] = next(input_buffer)
            else:
                yield param if param_1_mode == 'immediate' else memory[param]
            ip += 2

        elif opcode in (5, 6):
            param, jump_addr = memory[ip + 1:ip + 3]
            if param_1_mode == 'position':
                param = memory[param]
            if param_2_mode == 'position':
                jump_addr = memory[jump_addr]

            if (param and opcode == 5) or (param == 0 and opcode == 6):
                ip = jump_addr
            else:
                ip += 3

        else:
            raise ValueError('Unknown opcode')


if __name__ == '__main__':
    with open('puzzle_5_input') as f:
        initial_memory = [int(elem) for elem in f.read().split(',')]

    # Part 1
    outputs = execute_program(initial_memory.copy(), [1])
    print(list(outputs))

    # Part 2
    outputs = execute_program(initial_memory.copy(), [5])
    print(list(outputs))
