from intcode_computer import execute_program

if __name__ == '__main__':
    with open('puzzle_19_input') as f:
        memory = [int(elem) for elem in f.read().split(',')]

    result = sum(next(execute_program(memory.copy(), [x, y]))
                 for y in range(50)
                 for x in range(50))

    print(f'Solution: {result}')

    for y in range(1450, 2000):
        for x in range(1200, 1300):
            if next(execute_program(memory.copy(), [x, y])) \
                    and next(execute_program(memory.copy(), [x + 99, y])) \
                    and next(execute_program(memory.copy(), [x, y + 99])):
                print(f'Solution: {x*10000 + y}')
                break
        else:
            continue

        break

    # with open('img/puzzle_19_image_raw', 'wb') as f:
    #     for y in range(1570):
    #         print(y)
    #         f.write(bytes(next(execute_program(memory.copy(), [x, y]))
    #                       for x in range(1330)))
