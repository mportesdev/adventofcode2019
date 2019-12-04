import re

repeating_digits = re.compile(r'(\d)\1+')


def contains_doubles(n):
    return repeating_digits.search(f'{n:06}') is not None


def no_decrease(n):
    as_string = f'{n:06}'
    for i in range(1, len(as_string)):
        # we could compare ord() or int(), but this works, too
        if as_string[i] < as_string[i - 1]:
            return False

    return True


def contains_exact_double(n):
    for match_obj in repeating_digits.finditer(f'{n:06}'):
        if len(match_obj.group()) == 2:
            return True

    return False


if __name__ == '__main__':
    candidates = [n for n in range(130254, 678275 + 1)
                  if contains_doubles(n) and no_decrease(n)]

    # Part 1
    print(f'Solution: {len(candidates)}')

    narrowed_candidates = [n for n in candidates if contains_exact_double(n)]

    # Part 2
    print(f'Solution: {len(narrowed_candidates)}')
