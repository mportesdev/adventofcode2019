from puzzle_8 import get_layers, get_visible_pixel


def test_get_layers():
    layers = get_layers('123456789012', 3, 2)
    assert next(layers) == '123456'
    assert next(layers) == '789012'


def test_get_visible_pixel():
    assert get_visible_pixel(['0', '1', '2', '0']) == 0
    assert get_visible_pixel(['2', '1', '2', '0']) == 1
    assert get_visible_pixel(['2', '2', '1', '0']) == 1
    assert get_visible_pixel(['2', '2', '2', '0']) == 0
