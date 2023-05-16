n, k = map(int, input().split())
lines = [int(input()) for _ in range(n)]

start, end = 1, max(lines)
while start <= end:
    mid = (start + end) // 2

    count = sum([line // mid for line in lines])

    if count >= k:
        start = mid + 1
    else:
        end = mid - 1

print(end)
