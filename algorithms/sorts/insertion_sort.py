from util import exchange


def sort(a: list):
    size = len(a)
    i = 0
    while i < size:
        j = i
        while j > 0:
            if a[j] < a[j-1]:
                exchange(a, j, j-1)
            else:
                break
            j -= 1
        i += 1


x = [
    5, 7, 2, 11, 23, -1, 0, 1, 16
]
sort(x)
print(x)
