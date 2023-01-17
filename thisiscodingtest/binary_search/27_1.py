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
    if (mid == 0 or target > data[mid - 1]) and data[mid] == target:
        return mid
    elif target <= data[mid]:
        return first(data, target, start, mid - 1)
    else:
        return first(data, target, mid + 1, end)


def last(data, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    if (mid == n - 1 or target < data[mid + 1]) and data[mid] == target:
        return mid
    elif target < data[mid]:
        return last(data, target, start, mid - 1)
    else:
        return last(data, target, mid + 1, end)


def count_by_value(data, x):
    n = len(data)
    a = first(data, x, 0, n - 1)
    if a == None:
        return 0
    b = last(data, x, 0, n - 1)

    return b - a + 1


count = count_by_value(data, x)
print(count)

#
# from bisect import bisect_left, bisect_right
#
# n, x = map(int, input().split())
# array = list(map(int, input().split()))
#
#
# def count_by_value(array, x):
#     first_index = bisect_left(array, x)
#     last_index = bisect_right(array, x) - 1
#     return last_index - first_index + 1 if first_index <= last_index else -1
#
#
# print(count_by_value(array, x))
