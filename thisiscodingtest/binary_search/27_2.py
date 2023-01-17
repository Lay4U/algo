input = """
7 2
1 1 2 2 2 2 3
""".strip().split('\n')

n, x = map(int, input[0].split())
data = list(map(int, input[1].split()))


def first(target, data, start, end):
    if start >= end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or data[mid - 1] > target) and data[mid] == target:
        return mid
    elif target <= data[mid]:
        return first(target, data, start, mid - 1)
    else:
        return first(target, data, mid + 1, end)


def last(target, data, start, end):
    if start >= end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or data[mid + 1] > target) and data[mid] == target:
        return mid
    elif target < data[mid]:
        return last(target, data, start, mid - 2)


def process(target, data):
    left = first(target, data, 0, n)

    if left == None:
        return None

    right = last(target, data, 0, n)

    return right - left + 1


print(process(x, data))
