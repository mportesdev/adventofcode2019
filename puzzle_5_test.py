from puzzle_5 import decimal_digit, execute_program


def test_get_decimal_digit():
    assert decimal_digit(123, 0) == 3
    assert decimal_digit(123, 1) == 2
    assert decimal_digit(123, 2) == 1
    assert decimal_digit(123, 3) == 0

    assert decimal_digit(1101, 0) == 1
    assert decimal_digit(1101, 1) == 0
    assert decimal_digit(1101, 2) == 1
    assert decimal_digit(1101, 3) == 1
    assert decimal_digit(1101, 4) == 0
    assert decimal_digit(1101, 5) == 0


def test_execute_program():
    # opcode 3 and 4
    memory = [3, 0, 4, 0, 99]
    input_buffer = iter([68])
    output = execute_program(memory, input_buffer)
    assert list(output) == [68]
    assert memory == [68, 0, 4, 0, 99]

    # opcode 2 position + immediate
    memory = [1002, 4, 3, 4, 33]
    input_buffer = iter([])
    output = execute_program(memory, input_buffer)
    assert list(output) == []
    assert memory == [1002, 4, 3, 4, 99]


def test_execute_program_opcode_5():
    # opcode 5 immediate, test 0 is non-zero
    memory = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    input_buffer = iter([0])
    output = execute_program(memory, input_buffer)
    assert list(output) == [0]

    # opcode 5 immediate, test 68 is non-zero
    memory = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    input_buffer = iter([68])
    output = execute_program(memory, input_buffer)
    assert list(output) == [1]


def test_execute_program_opcode_6():
    # opcode 6, test 0 is zero
    memory = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    input_buffer = iter([0])
    output = execute_program(memory, input_buffer)
    assert list(output) == [0]

    # opcode 6, test 68 is zero
    memory = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    input_buffer = iter([68])
    output = execute_program(memory, input_buffer)
    assert list(output) == [1]


def test_execute_program_opcode_7():
    # opcode 7, test 5 < 8
    memory = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    input_buffer = iter([5])
    output = execute_program(memory, input_buffer)
    assert list(output) == [1]

    # opcode 7, test 8 < 8
    memory = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    input_buffer = iter([8])
    output = execute_program(memory, input_buffer)
    assert list(output) == [0]

    # opcode 7 immediate, test 5 < 8
    memory = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    input_buffer = iter([5])
    output = execute_program(memory, input_buffer)
    assert list(output) == [1]

    # opcode 7 immediate, test 8 < 8
    memory = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    input_buffer = iter([8])
    output = execute_program(memory, input_buffer)
    assert list(output) == [0]


def test_execute_program_opcode_8():
    # opcode 8, test 8 == 8
    memory = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    input_buffer = iter([8])
    output = execute_program(memory, input_buffer)
    assert list(output) == [1]

    # opcode 8, test 5 == 8
    memory = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    input_buffer = iter([5])
    output = execute_program(memory, input_buffer)
    assert list(output) == [0]

    # opcode 8 immediate, test 8 == 8
    memory = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    input_buffer = iter([8])
    output = execute_program(memory, input_buffer)
    assert list(output) == [1]

    # opcode 8 immediate, test 5 == 8
    memory = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    input_buffer = iter([5])
    output = execute_program(memory, input_buffer)
    assert list(output) == [0]


def test_execute_program_larger_example():
    # input below 8
    memory = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20,
              31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46,
              104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98,
              99]
    input_buffer = iter([6])
    output = execute_program(memory, input_buffer)
    assert list(output) == [999]

    # input 8
    memory = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20,
              31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46,
              104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98,
              99]
    input_buffer = iter([8])
    output = execute_program(memory, input_buffer)
    assert list(output) == [1000]

    # input below 8
    memory = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20,
              31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46,
              104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98,
              99]
    input_buffer = iter([68])
    output = execute_program(memory, input_buffer)
    assert list(output) == [1001]
