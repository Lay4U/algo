n, m = 4, 7
datas = [20, 15, 10, 17]

start = 1
end = max(datas)

while start <= end:
    mid = (start + end) // 2
    print(start, end, mid)
    if sum(data - mid if data > mid else 0 for data in datas) >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
