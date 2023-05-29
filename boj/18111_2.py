n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

min_height = min(map(min, land))
max_height = max(map(max, land))

min_time = float('inf')
max_land = 0

for h in range(min_height, max_height + 1):
    time = 0
    inventory = b
    for i in range(n):
        for j in range(m):
            if land[i][j] < h:
                time += (h - land[i][j])
                inventory -= (h - land[i][j])
            else:
                time += (land[i][j] - h) * 2
                inventory += (land[i][j] - h)
    if inventory >= 0:
        if time <= min_time:
            min_time = time
            max_land = h

print(min_time, max_land)
