from math import pi
from pytest import approx

from puzzle_10 import polar_coordinates, directly_visible


def test_polar_coordinates():
    two_sqrt = round(2 ** 0.5, 6)
    assert polar_coordinates(1, 0) == approx((pi / 2, 1))
    assert polar_coordinates(1, 1) == approx((pi * 3 / 4, two_sqrt))
    assert polar_coordinates(0, 1) == approx((pi, 1))
    assert polar_coordinates(-1, 1) == approx((pi * 5 / 4, two_sqrt))
    assert polar_coordinates(-1, 0) == approx((pi * 3 / 2, 1))
    assert polar_coordinates(-1, -1) == approx((pi * 7 / 4, two_sqrt))
    assert polar_coordinates(0, -1) == approx((0, 1))
    assert polar_coordinates(1, -1) == approx((pi / 4, two_sqrt))


def test_directly_visible():
    map_data = (""".#..#
.....
#####
....#
...##""").splitlines()
    assert directly_visible(map_data, 3, 4) == 8
    assert directly_visible(map_data, 1, 0) == 7
    assert directly_visible(map_data, 0, 2) == 6
    assert directly_visible(map_data, 4, 2) == 5

    map_data = ("""......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####""").splitlines()
    assert directly_visible(map_data, 5, 8) == 33

    map_data = ("""#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.""").splitlines()
    assert directly_visible(map_data, 1, 2) == 35

    map_data = (""".#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..""").splitlines()
    assert directly_visible(map_data, 6, 3) == 41

    map_data = (""".#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""").splitlines()
    assert directly_visible(map_data, 11, 13) == 210
