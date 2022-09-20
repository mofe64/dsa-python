from util import exchange


def sort(a: list):
    size = len(a)
    for i in range(size):
        for j in range(i + 1, size):
            if a[i] > a[j]:
                exchange(a, i, j)


x = [1, 3, 0, 11, 3, 5, 6, -1, -2, 78, 10]
sort(x)
print(x)
