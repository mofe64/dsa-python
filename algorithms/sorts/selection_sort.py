from re import I
from util import exchange


def sort(a: list):
    size = len(a)
    index_of_current_value = 0
    while index_of_current_value < size:
        index_of_min_value = index_of_current_value
        index_of_value_to_compare = index_of_current_value + 1
        while index_of_value_to_compare < size:
            if a[index_of_value_to_compare] < a[index_of_min_value]:
                index_of_min_value = index_of_value_to_compare
            index_of_value_to_compare += 1
        exchange(a, index_of_current_value, index_of_min_value)
        index_of_current_value += 1


x = [
    5, 7, 2, 11, 23, -1, 0, 1, 16
]
sort(x)
print(x)
