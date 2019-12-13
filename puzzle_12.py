from math import gcd
import re


class Moon:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.position = [x, y, z]
        self.velocity = [0, 0, 0]

    def apply_gravity(self, other) -> None:
        self.velocity[0] += gravity_pull(other.position[0] - self.position[0])
        self.velocity[1] += gravity_pull(other.position[1] - self.position[1])
        self.velocity[2] += gravity_pull(other.position[2] - self.position[2])

    def apply_velocity(self) -> None:
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]

    def potential_energy(self) -> int:
        return sum(abs(n) for n in self.position)

    def kinetic_energy(self) -> int:
        return sum(abs(n) for n in self.velocity)

    def total_energy(self) -> int:
        return self.potential_energy() * self.kinetic_energy()


def gravity_pull(n: int) -> int:
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0


def get_coords(vector_string: str) -> list:
    str_numerals = re.findall(r'[+-]?\d+', vector_string)
    return [int(s) for s in str_numerals]


def moons_from_data(input_data: str) -> list:
    return [Moon(*get_coords(line)) for line in input_data.splitlines()]


def simulate_one_step(moons: list) -> None:
    for moon in moons:
        for other in moons:
            if other is not moon:
                moon.apply_gravity(other)

    for moon in moons:
        moon.apply_velocity()


if __name__ == '__main__':
    with open('puzzle_12_input') as f:
        input_data = f.read()

    # Part 1
    moons = moons_from_data(input_data)

    for i in range(1000):
        simulate_one_step(moons)

    print(f'Solution: {sum(m.total_energy() for m in moons)}')

    # Part 2
    moons = moons_from_data(input_data)

    initial_x = [m.position[0] for m in moons]
    initial_y = [m.position[1] for m in moons]
    initial_z = [m.position[2] for m in moons]

    period_x, period_y, period_z = None, None, None
    steps = 0

    while True:
        simulate_one_step(moons)
        steps += 1

        if period_x is None and [m.position[0] for m in moons] == initial_x \
                and not any(m.velocity[0] for m in moons):
            print(f'Period for x found: {steps}')
            period_x = steps

        if period_y is None and [m.position[1] for m in moons] == initial_y \
                and not any(m.velocity[1] for m in moons):
            print(f'Period for y found: {steps}')
            period_y = steps

        if period_z is None and [m.position[2] for m in moons] == initial_z \
                and not any(m.velocity[2] for m in moons):
            print(f'Period for z found: {steps}')
            period_z = steps

        if all((period_x, period_y, period_z)):
            break

    # greatest common denominator for the 3 values
    gcd_all = min((gcd(period_x, period_y), gcd(period_x, period_z),
                   gcd(period_y, period_z)))

    # least common multiple for the 3 values
    lcm = (period_x // gcd_all) * (period_y // gcd_all) * (period_z // gcd_all)
    print(f'Solution: {lcm}')
