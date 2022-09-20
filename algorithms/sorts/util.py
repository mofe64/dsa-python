def is_lesser_than(value_one, value_two) -> bool:
    return value_one < value_two


def exchange(a: list, i, j):
    swap = a[i]
    a[i] = a[j]
    a[j] = swap
