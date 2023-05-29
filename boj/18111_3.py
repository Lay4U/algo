from collections import Counter

n, m, b = map(int, input().split())
land = [map(int, input().split()) for _ in range(n)]

flat_land = [height for row in land for height in row]
# print(flat_land)
counter = Counter(flat_land)
# print(counter)
# print(counter.items())

min_time = 1e9
max_height = 0

for h in range(257):
    time = 0
    inventory = b
    for height, freq in counter.items():
        if height < h:
            time += (h - height) * freq
            inventory -= (h - height) * freq
        else:
            time += (height - h) * 2 * freq
            inventory += (height - h) * freq

    if inventory >= 0:
        if min_time >= time:
            min_time = time
            max_height = h

print(min_time, max_height)

# min_height = min(map(min, land))
# max_height = max(map(max, land))
#
# min_time = 1e9
# max_land = 0
# for h in range(min_height, max_height+1):
#     time = 0
#     inventory = b
#     for i in range(n):
#         for j in range(m):
#             if land[i][j] < h:
#                 time += (h - land[i][j])
#                 inventory += (h - land[i][j])
#             else:
#                 time += (land[i][j] - h) * 2
#                 inventory -= (land[i][j] - h)
#
#     if inventory >= 0:
#         if min_time > time:
#             min_time = time
#             max_land = h
#
