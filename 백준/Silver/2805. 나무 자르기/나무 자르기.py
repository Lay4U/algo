n, m = map(int, input().split())
datas = list(map(int, input().split()))

start, end = 0, max(datas)

while start <= end:
    mid = (start + end) // 2
    total = sum(data - mid if data > mid else 0 for data in datas)
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
