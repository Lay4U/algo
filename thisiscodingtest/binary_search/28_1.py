input = """
7
-15 -4 2 8 9 13 15
""".strip().split('\n')

n = int(input[0])
data = list(map(int, input[1].split()))
print(data)


def bs(data, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # print(mid, data[mid])
    if mid == data[mid]:
        return mid
    elif data[mid] > mid:
        return bs(data, start, mid - 1)
    else:
        return bs(data, mid + 1, end)


print("---")
print(bs(data, 0, n - 1))
