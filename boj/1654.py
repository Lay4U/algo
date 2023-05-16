# 4 11
# 802
# 743
# 457
# 539
k, n = 4, 11
lan = [802, 743, 457, 539]
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in lan:
        lines += i // mid
    print(start, end, mid, lines)
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
