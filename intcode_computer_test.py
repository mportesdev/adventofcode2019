from intcode_computer import decimal_digit, memory_read, memory_write, \
                             execute_program


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


def test_memory_read():
    memory = [1, 2, 3]
    assert memory_read(memory, 5) == 0
    assert memory == [1, 2, 3, 0, 0, 0]

    assert memory_read(memory, 0) == 1

    assert memory_read(memory, 10) == 0
    assert memory == [1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0]


def test_memory_write():
    memory = [1, 2, 3]
    memory_write(memory, 0, 5)
    assert memory == [5, 2, 3]

    memory_write(memory, 3, 6)
    assert memory == [5, 2, 3, 6]

    memory_write(memory, 10, 7)
    assert memory == [5, 2, 3, 6, 0, 0, 0, 0, 0, 0, 7]


def test_execute_program_day_5():
    # opcode 3 and 4
    memory = [3, 0, 4, 0, 99]
    output = list(execute_program([memory, 0], [68]))
    assert output == [68]
    assert memory == [68, 0, 4, 0, 99]

    # opcode 2, position + immediate
    memory = [1002, 4, 3, 4, 33]
    output = list(execute_program([memory, 0], []))
    assert output == []
    assert memory == [1002, 4, 3, 4, 99]

    # opcode 5 immediate, test 0 is non-zero
    memory = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    input_buffer = [0]
    output = list(execute_program([memory, 0], input_buffer))
    assert output == [0]

    # opcode 5 immediate, test 68 is non-zero
    memory = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    input_buffer = [68]
    output = list(execute_program([memory, 0], input_buffer))
    assert output == [1]

    # opcode 6, test 0 is zero
    memory = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    input_buffer = [0]
    output = list(execute_program([memory, 0], input_buffer))
    assert output == [0]

    # opcode 6, test 68 is zero
    memory = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    input_buffer = [68]
    output = list(execute_program([memory, 0], input_buffer))
    assert output == [1]

    # opcode 7, test 5 < 8
    memory = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    input_buffer = [5]
    output = list(execute_program([memory, 0], input_buffer))
    assert output == [1]

    # opcode 7, test 8 < 8
    memory = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    input_buffer = [8]
    output = list(execute_program([memory, 0], input_buffer))
    assert output == [0]

    # opcode 7 immediate, test 5 < 8
    memory = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    input_buffer = [5]
    output = list(execute_program([memory, 0], input_buffer))
    assert output == [1]

    # opcode 7 immediate, test 8 < 8
    memory = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    input_buffer = [8]
    output = list(execute_program([memory, 0], input_buffer))
    assert output == [0]

    # opcode 8, test 8 == 8
    memory = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    input_buffer = [8]
    output = list(execute_program([memory, 0], input_buffer))
    assert output == [1]

    # opcode 8, test 5 == 8
    memory = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    input_buffer = [5]
    output = list(execute_program([memory, 0], input_buffer))
    assert output == [0]

    # opcode 8 immediate, test 8 == 8
    memory = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    input_buffer = [8]
    output = list(execute_program([memory, 0], input_buffer))
    assert output == [1]

    # opcode 8 immediate, test 5 == 8
    memory = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    input_buffer = [5]
    output = list(execute_program([memory, 0], input_buffer))
    assert output == [0]

    # input below 8
    memory = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20,
              31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46,
              104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98,
              99]
    input_buffer = [6]
    output = list(execute_program([memory, 0], input_buffer))
    assert output == [999]

    # input 8
    memory = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20,
              31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46,
              104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98,
              99]
    input_buffer = [8]
    output = list(execute_program([memory, 0], input_buffer))
    assert output == [1000]

    # input below 8
    memory = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20,
              31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46,
              104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98,
              99]
    input_buffer = [68]
    output = list(execute_program([memory, 0], input_buffer))
    assert output == [1001]


def test_execute_program_day_9():
    memory = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006,
              101, 0, 99]
    output = list(execute_program([memory.copy(), 0], []))
    assert output == memory

    memory = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
    output = list(execute_program([memory.copy(), 0], []))
    assert len(output) == 1
    assert len(str(output[0])) == 16

    memory = [104, 1125899906842624, 99]
    output = list(execute_program([memory.copy(), 0], []))
    assert len(output) == 1
    assert output[0] == 1125899906842624
