from puzzle_1 import fuel_from_mass


def test_fuel_from_mass():
    assert fuel_from_mass(0) == 0
    assert fuel_from_mass(1) == 0
    assert fuel_from_mass(5) == 0
    assert fuel_from_mass(100) == 31
    assert fuel_from_mass(130129) == 43374
