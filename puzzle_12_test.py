from puzzle_12 import get_coords, simulate_one_step, moons_from_data


def test_get_coords():
    assert get_coords('<x=-1, y=0, z=2>') == [-1, 0, 2]
    assert get_coords('<x=2, y=-10, z=-7>') == [2, -10, -7]
    assert get_coords('<x=4, y=-8, z=8>') == [4, -8, 8]
    assert get_coords('<x=3, y=5, z=-1>') == [3, 5, -1]


def test_simulate_one_step_example_1():
    input_data = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
    moons = moons_from_data(input_data)
    for i in range(10):
        simulate_one_step(moons)
    assert moons[0].position == [2, 1, -3]
    assert moons[0].velocity == [-3, -2, 1]
    assert moons[1].position == [1, -8, 0]
    assert moons[1].velocity == [-1, 1, 3]
    assert moons[2].position == [3, -6, 1]
    assert moons[2].velocity == [3, 2, -3]
    assert moons[3].position == [2, 0, 4]
    assert moons[3].velocity == [1, -1, -1]

    assert moons[0].total_energy() == 36
    assert moons[1].total_energy() == 45
    assert moons[2].total_energy() == 80
    assert moons[3].total_energy() == 18


def test_simulate_one_step_example_2():
    input_data = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""
    moons = moons_from_data(input_data)
    for i in range(100):
        simulate_one_step(moons)
    assert moons[0].position == [8, -12, -9]
    assert moons[0].velocity == [-7, 3, 0]
    assert moons[1].position == [13, 16, -3]
    assert moons[1].velocity == [3, -11, -5]
    assert moons[2].position == [-29, -11, -1]
    assert moons[2].velocity == [-3, 7, 4]
    assert moons[3].position == [16, -13, 23]
    assert moons[3].velocity == [7, 1, 1]

    assert moons[0].total_energy() == 290
    assert moons[1].total_energy() == 608
    assert moons[2].total_energy() == 574
    assert moons[3].total_energy() == 468
