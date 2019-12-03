from puzzle_3 import inclusive_range


def test_inclusive_range():
    assert inclusive_range(0) == range(1)

    assert inclusive_range(1) == range(2)
    assert inclusive_range(-1) == range(0, -2, -1)

    assert inclusive_range(1000) == range(1001)
    assert inclusive_range(-1000) == range(0, -1001, -1)

    assert list(inclusive_range(4)) == [0, 1, 2, 3, 4]
    assert list(inclusive_range(-4)) == [0, -1, -2, -3, -4]
