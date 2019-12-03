from puzzle_3 import inclusive_range, route_from_vectors, vector_from_string


def test_inclusive_range():
    assert inclusive_range(0) == range(1)
    assert list(inclusive_range(0)) == [0]

    assert inclusive_range(1) == range(2)
    assert list(inclusive_range(1)) == [0, 1]

    assert inclusive_range(-1) == range(0, -2, -1)
    assert list(inclusive_range(-1)) == [0, -1]

    assert 1000 in inclusive_range(1000)
    assert -1000 in inclusive_range(-1000)

    assert inclusive_range(1_000_000) == range(1_000_001)
    assert inclusive_range(-1_000_000) == range(0, -1_000_001, -1)

    assert list(inclusive_range(8)) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert list(inclusive_range(-8)) == [0, -1, -2, -3, -4, -5, -6, -7, -8]


def test_vector_from_string():
    result = [vector_from_string(item) for item in 'R8,U5,L5,D3'.split(',')]

    expected = [(8, 0), (0, -5), (-5, 0), (0, 3)]

    assert result == expected


def test_route_from_vectors():
    vectors = [(8, 0), (0, -5), (-5, 0), (0, 3)]
    result = route_from_vectors(vectors)

    expected = [
        (0, 0),
        (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),
        (8, -1), (8, -2), (8, -3), (8, -4), (8, -5),
        (7, -5), (6, -5), (5, -5), (4, -5), (3, -5),
        (3, -4), (3, -3), (3, -2),
    ]

    assert result == expected
