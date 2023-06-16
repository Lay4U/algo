n, k = map(int, input().split())
datas = []
for i in range(n):
    datas.append(int(input()))

start, end = 1, max(datas)

while start <= end:
    mid = (start + end) // 2

    total = sum([data // mid for data in datas])

    if total >= k:
        start = mid + 1
    else:
        end = mid - 1

print(end)
