k, n = map(int, input().split())
data = [int(input()) for _ in range(k)]
start, end = 0, max(data)

while start <= end:
    mid = (start + end) // 2
    count = sum(d // mid for d in data)

    if count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
