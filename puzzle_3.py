from itertools import product


def vector_from_string(input_str):
    direction, distance = input_str[0], int(input_str[1:])
    vector = {
                'U': (0, -distance), 'D': (0, distance),
                'L': (-distance, 0), 'R': (distance, 0),
             }[direction]

    return vector


def route_from_vectors(vectors):
    route = []
    current_position = (0, 0)

    for dist_x, dist_y in vectors:
        step_x = 1 if dist_x >= 0 else -1
        step_y = 1 if dist_y >= 0 else -1
        first_on_segment = True

        for point in product(range(0, dist_x + step_x, step_x),
                             range(0, dist_y + step_y, step_y)):
            point_on_route = (current_position[0] + point[0],
                              current_position[1] + point[1])

            # do not repeat corner points, but do include starting point
            if first_on_segment:
                first_on_segment = False
                if route:
                    continue
            route.append(point_on_route)

        current_position = point_on_route

    return route


def routes_from_input_data(input_data):
    vectors_1, vectors_2 = [[vector_from_string(item)
                             for item in line.split(',')]
                            for line in input_data.splitlines()]

    route_1 = route_from_vectors(vectors_1)
    route_2 = route_from_vectors(vectors_2)
    return route_1, route_2


def manhattan(point):
    return abs(point[0]) + abs(point[1])


def solution_part_1(input_data):
    route_1, route_2 = routes_from_input_data(input_data)
    intersections = (set(route_1) & set(route_2)) - {(0, 0)}

    return min(map(manhattan, intersections))


def solution_part_2(input_data):
    route_1, route_2 = routes_from_input_data(input_data)
    intersections = (set(route_1) & set(route_2)) - {(0, 0)}

    return min(route_1.index(intersection) + route_2.index(intersection)
               for intersection in intersections)


if __name__ == '__main__':
    # sample data
    data_1 = 'R8,U5,L5,D3\nU7,R6,D4,L4\n'
    assert solution_part_1(data_1) == 6
    assert solution_part_2(data_1) == 30

    data_2 = ('R75,D30,R83,U83,L12,D49,R71,U7,L72\n'
              'U62,R66,U55,R34,D71,R55,D58,R83\n')
    assert solution_part_1(data_2) == 159
    assert solution_part_2(data_2) == 610

    data_3 = ('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n'
              'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7\n')
    assert solution_part_1(data_3) == 135
    assert solution_part_2(data_3) == 410

    # my input data
    with open('puzzle_3_input') as f:
        data = f.read()

    # Part 1
    print(f'Solution: {solution_part_1(data)}')

    # Part 2
    print(f'Solution: {solution_part_2(data)}')
