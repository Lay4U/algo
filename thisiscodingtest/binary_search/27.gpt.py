from bisect import bisect_left, bisect_right


def count_by_value(array, x):
    first_index = bisect_left(array, x)
    last_index = bisect_right(array, x) - 1
    return last_index - first_index + 1 if first_index <= last_index else -1


n, x = map(int, input().split())
array = list(map(int, input().split()))

print(count_by_value(array, x))
