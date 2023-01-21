from bisect import bisect_left, bisect_right

input = """
7 2
1 1 2 2 2 2 3
""".strip().split('\n')

n, x = map(int, input[0].split())

data = list(map(int, input[1].split()))


def first(data, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if (mid == 0 or data[mid - 1] < target) and data[mid] == target:
        return mid
    elif data[mid] >= target:
        return first(data, target, start, mid - 1)
    else:
        return first(data, target, mid + 1, end)


def last(data, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if (mid == 0 or data[mid + 1] > target) and data[mid] == target:
        return mid
    elif data[mid] > target:
        return last(data, target, start, mid - 1)
    else:
        return last(data, target, mid + 1, end)


def process(data, target):
    idxFirst = first(data, target, 0, n - 1)
    if idxFirst is None:
        return None
    idxLast = last(data, target, 0, n - 1)

    return idxLast - idxFirst + 1


print(process(data, x))

a = bisect_left(data, x)
b = bisect_right(data, x) - 1
print(a, b)

print(b - a + 1)
