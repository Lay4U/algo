k, n = map(int, input().split())
datas = [int(input()) for _ in range(k)]

start, end = 1, max(datas)

while start <= end:
    mid = (start + end) // 2

    total = sum(data // mid for data in datas)

    if total >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
