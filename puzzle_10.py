from math import acos, pi


def polar_coordinates(dx, dy):
    dist = (dx**2 + dy**2) ** 0.5
    angle = acos(dx / dist)

    if dy < 0:
        angle += 2 * (pi - angle)

    # adjust for upward direction, e.g. (dx=0, dy=-1), to be angle 0
    angle = (angle + pi/2) % (2 * pi)

    return round(angle, 6), round(dist, 6)


def group_by_angle(map_data, x, y):
    result = {}
    for ast_y, row in enumerate(map_data):
        for ast_x, char in enumerate(row):
            if char == '#' and (ast_x != x or ast_y != y):
                angle, dist = polar_coordinates(ast_x - x, ast_y - y)
                result.setdefault(angle, set()).add((dist, ast_x, ast_y))

    return result


def directly_visible(map_data, x, y):
    return len(group_by_angle(map_data, x, y))


if __name__ == '__main__':
    with open('puzzle_10_input') as f:
        map_data = f.read().splitlines()

    # Part 1
    counts_of_visible = ((directly_visible(map_data, x, y), x, y)
                         for y, row in enumerate(map_data)
                         for x, char in enumerate(row)
                         if char == '#')

    n, base_x, base_y = max(counts_of_visible)
    print(f'Solution: {n}')

    # Part 2
    asteroid_data = group_by_angle(map_data, base_x, base_y)
    counter = 0
    to_vaporize = ''.join(map_data).count('#') - 1

    while True:
        for angle in sorted(asteroid_data):
            data_for_angle = asteroid_data[angle]
            if data_for_angle:
                nearest = min(data_for_angle)
                data_for_angle.remove(nearest)
                x, y = nearest[1:]
                counter += 1
                if counter == 200:
                    print(f'Solution: {100*x + y}')
        if counter == to_vaporize:
            break
