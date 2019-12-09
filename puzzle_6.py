def dict_from_data(data: str) -> dict:
    result = {}
    for line in data.splitlines():
        parent, child = line.split(')')
        result.setdefault(parent, []).append(child)

    return result


def direct_orbits(data_dict: dict, parent='COM') -> int:
    if parent not in data_dict:
        return 0

    children = data_dict[parent]
    result = len(children)
    for child in children:
        result += direct_orbits(data_dict, child)

    return result


def total_orbits(data_dict: dict) -> int:
    return sum(direct_orbits(data_dict, parent) for parent in data_dict)


def steps_to_child(data_dict, obj_from, wanted_child):
    # if not in keys, has no child objects at all
    if obj_from not in data_dict:
        return -1

    if wanted_child in data_dict[obj_from]:
        return 1

    for child in data_dict[obj_from]:
        steps = steps_to_child(data_dict, child, wanted_child)
        if steps != -1:
            return 1 + steps

    return -1


def transfers(data_dict, obj_from, obj_to):
    steps_back = 0

    # move to the common parent object, counting steps
    while (steps_forward := steps_to_child(data_dict, obj_from, obj_to)) == -1:
        # find direct parent
        for parent, children in data_dict.items():
            if obj_from in children:
                steps_back += 1
                obj_from = parent
                break

    return steps_back + steps_forward


if __name__ == '__main__':
    with open('puzzle_6_input') as f:
        input_data = f.read()

    data_dict = dict_from_data(input_data)

    # Part 1
    print(f'Solution: {total_orbits(data_dict)}')

    # Part 2
    print(f'Solution: {transfers(data_dict, "YOU", "SAN") - 2}')
