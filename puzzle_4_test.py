from puzzle_4 import contains_doubles, no_decrease, contains_exact_double


def test_contains_doubles():
    assert contains_doubles(111111)
    assert contains_doubles(122345)

    assert not contains_doubles(123789)
    assert not contains_doubles(626262)

    assert contains_doubles(311133)
    assert contains_doubles(332211)
    assert contains_doubles(811622)

    assert contains_doubles(1)
    assert contains_doubles(4567)


def test_no_decrease():
    assert no_decrease(111123)
    assert no_decrease(135679)

    assert no_decrease(111111)
    assert no_decrease(123456)

    assert not no_decrease(223450)
    assert not no_decrease(889998)


def test_contains_exact_double():
    assert contains_exact_double(112233)
    assert not contains_exact_double(123444)
    assert contains_exact_double(111122)

    assert contains_exact_double(877666)
    assert not contains_exact_double(999999)

    assert contains_exact_double(1234)
    assert not contains_exact_double(999)
