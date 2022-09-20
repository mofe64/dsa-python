from util import exchange


def sort(a: list):
    size = len(a)
    index_of_current_value = 0
    while index_of_current_value < size:
        index_of_value_to_compare = index_of_current_value
        # At this point we want to compare the current value with all previous values
        # This is to ensure that all values to the left of the array are sorted properly
        # So to get all previous values we decrement the index of current value till we get to 0
        while index_of_value_to_compare > 0:
            if a[index_of_value_to_compare] < a[index_of_value_to_compare-1]:
                exchange(a, index_of_value_to_compare,
                         index_of_value_to_compare-1)
            else:
                break
            index_of_value_to_compare -= 1
        index_of_current_value += 1


x = [
    5, 7, 2, 11, 23, -1, 0, 1, 16
]
sort(x)
print(x)
