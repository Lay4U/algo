n, m = 4, 7
datas = [20, 15, 10, 17]

start, end = 0, max(datas)

while start <= end:
    mid = (start + end) // 2

    count = sum(data - mid for data in datas if data > mid)

    if count >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
