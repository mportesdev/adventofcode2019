def decimal_digit(n: int, order: int) -> int:
    return (n // 10**order) % 10


def memory_read(memory, address):
    extend_by = address - len(memory) + 1
    if extend_by > 0:
        memory.extend([0] * extend_by)

    return memory[address]


def memory_write(memory, address, value):
    extend_by = address - len(memory) + 1
    if extend_by > 0:
        memory.extend([0] * extend_by)

    memory[address] = value


def execute_program(memory, input_buffer: list):
    ip = 0
    relative_base = 0

    dispatch_dict = {1: lambda x, y: x + y,
                     2: lambda x, y: x * y,
                     7: lambda x, y: 1 if x < y else 0,
                     8: lambda x, y: 1 if x == y else 0}

    param_modes = {0: 'position', 1: 'immediate', 2: 'relative'}

    while (opcode := memory[ip]) != 99:
        param_1_mode = param_modes[decimal_digit(opcode, 2)]
        param_2_mode = param_modes[decimal_digit(opcode, 3)]
        param_3_mode = param_modes[decimal_digit(opcode, 4)]
        opcode = opcode % 100

        if opcode in (1, 2, 7, 8):
            # opcodes with 3 parameters (2 values + 1 address)
            param_1, param_2, target_addr = memory[ip + 1:ip + 4]
            ip += 4

            if param_1_mode == 'position':
                param_1 = memory_read(memory, param_1)
            elif param_1_mode == 'relative':
                param_1 = memory[relative_base + param_1]

            if param_2_mode == 'position':
                param_2 = memory[param_2]
            elif param_2_mode == 'relative':
                param_2 = memory[relative_base + param_2]

            if param_3_mode == 'relative':
                target_addr = relative_base + target_addr

            memory_write(memory, target_addr,
                         dispatch_dict[opcode](param_1, param_2))

        elif opcode in (3, 4, 9):
            # opcodes with 1 parameter
            param = memory_read(memory, ip + 1)
            ip += 2

            if opcode == 3:
                # input
                if param_1_mode == 'relative':
                    param = relative_base + param

                value = input_buffer.pop(0)
                memory_write(memory, param, value)
            else:
                if param_1_mode == 'position':
                    param = memory_read(memory, param)
                elif param_1_mode == 'relative':
                    param = memory_read(memory, relative_base + param)

                if opcode == 4:
                    # output
                    yield param

                else:
                    relative_base += param

        elif opcode in (5, 6):
            # opcodes with 2 parameters (1 value + 1 address)
            param, jump_addr = memory[ip + 1:ip + 3]
            ip += 3

            if param_1_mode == 'position':
                param = memory[param]
            elif param_1_mode == 'relative':
                param = memory[relative_base + param]

            if param_2_mode == 'position':
                jump_addr = memory[jump_addr]
            elif param_2_mode == 'relative':
                jump_addr = memory[relative_base + jump_addr]

            if (param and opcode == 5) or (param == 0 and opcode == 6):
                ip = jump_addr

        else:
            raise ValueError(f'Unknown opcode: {opcode}')
