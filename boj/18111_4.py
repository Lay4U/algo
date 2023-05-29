from collections import Counter

n, m, b = 3, 4, 0
land = [
    [64, 64, 64, 64],
    [64, 64, 64, 64],
    [64, 64, 64, 63],
]

flat_land = [height for row in land for height in row]
counter = Counter(flat_land)

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
        if time <= min_time:
            min_time = time
            max_height = h
