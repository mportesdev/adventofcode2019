# Part 1


def execute_program(memory):
    # instruction pointer
    ip = 0

    while True:
        opcode = memory[ip]
        if opcode == 99:
            return memory
        elif opcode in (1, 2):
            addr_1, addr_2, target_addr = memory[ip + 1:ip + 4]
            memory[target_addr] = (memory[addr_1] + memory[addr_2]
                                   if opcode == 1
                                   else memory[addr_1] * memory[addr_2])
            ip += 4


with open('puzzle_2_input') as f:
    memory = [int(elem) for elem in f.read().split(',')]

memory[1:3] = [12, 2]
print(f'Solution: {execute_program(memory)[0]}')


# Part 2

from itertools import product

with open('puzzle_2_input') as f:
    initial_state = [int(elem) for elem in f.read().split(',')]

# brute force search for the desired output of 19690720
for noun, verb in product(range(100), range(100)):
    memory = initial_state[:]
    memory[1:3] = [noun, verb]
    if execute_program(memory)[0] == 19690720:
        print(f'Solution: {100*noun + verb}')
        break
