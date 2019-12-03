from puzzle_3 import inclusive_range


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
