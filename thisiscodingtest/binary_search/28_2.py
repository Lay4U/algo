input = """
7
-15 -4 2 8 9 13 15
""".strip().split('\n')

n = int(input[0])
data = list(map(int, input[1].split()))

start = 0
end = n - 1
while True:
    if start > end:
        break
    mid = (start + end) // 2
    if mid == data[mid]:
        print(mid)
        break
    elif mid > data[mid]:
        start = mid - 1
    else:
        end = mid + 1
