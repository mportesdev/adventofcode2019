import pytest

from puzzle_6 import dict_from_data, direct_orbits, total_orbits, \
                     transfers, steps_to_child


@pytest.fixture
def dict_minimal_example():
    return {'COM': ['A'],
            'A': ['B', 'C']}


@pytest.fixture
def dict_example_1():
    return {'COM': ['B'],
            'B': ['C', 'G'],
            'C': ['D'],
            'D': ['E', 'I'],
            'E': ['F', 'J'],
            'G': ['H'],
            'J': ['K'],
            'K': ['L']}


@pytest.fixture
def dict_example_2():
    return {'COM': ['B'],
            'B': ['C', 'G'],
            'C': ['D'],
            'D': ['E', 'I'],
            'E': ['F', 'J'],
            'G': ['H'],
            'I': ['SAN'],
            'J': ['K'],
            'K': ['L', 'YOU']}


def test_dict_from_data(dict_minimal_example, dict_example_1, dict_example_2):
    data = """COM)A
A)B
A)C"""
    assert dict_from_data(data) == dict_minimal_example

    data = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""
    assert dict_from_data(data) == dict_example_1

    data = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""
    assert dict_from_data(data) == dict_example_2


def test_direct_orbits(dict_minimal_example, dict_example_1):
    assert direct_orbits(dict_minimal_example) == 3

    assert direct_orbits(dict_example_1) == 11


def test_total_orbits(dict_minimal_example, dict_example_1):
    assert total_orbits(dict_minimal_example) == 5

    assert total_orbits(dict_example_1) == 42


def test_transfers(dict_minimal_example, dict_example_2):
    assert transfers(dict_minimal_example, 'B', 'C') == 2

    assert transfers(dict_example_2, 'YOU', 'SAN') == 6
    assert transfers(dict_example_2, 'K', 'I') == 4


def test_steps_to_child(dict_minimal_example, dict_example_2):
    assert steps_to_child(dict_minimal_example, 'COM', 'A') == 1
    assert steps_to_child(dict_minimal_example, 'COM', 'B') == 2
    assert steps_to_child(dict_minimal_example, 'A', 'C') == 1
    assert steps_to_child(dict_minimal_example, 'B', 'C') == -1

    assert steps_to_child(dict_example_2, 'D', 'YOU') == 4
    assert steps_to_child(dict_example_2, 'D', 'SAN') == 2
    assert steps_to_child(dict_example_2, 'K', 'I') == -1
