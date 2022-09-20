from util import exchange


def sort(a: list):
    size = len(a)
    for i in range(size):
        for j in range(i + 1, size):
            if a[i] > a[j]:
                exchange(a, i, j)


x = [
    5, 7, 2, 11, 23, -1, 0, 1, 16
]
sort(x)
print(x)
