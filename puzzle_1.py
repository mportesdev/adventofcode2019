# Part 1


def fuel_from_mass(mass: int) -> int:
    return max(mass // 3 - 2, 0)


with open('puzzle_1_input') as f:
    print(f'Solution: {sum(fuel_from_mass(int(line)) for line in f)}')


# Part 2


def fuel_from_mass_2(mass: int) -> int:
    result = 0
    while (fuel := mass // 3 - 2) > 0:
        result += fuel
        mass = fuel
    return result


with open('puzzle_1_input') as f:
    print(f'Solution: {sum(fuel_from_mass_2(int(line)) for line in f)}')
