import sys
from collections import Counter

input = sys.stdin.readline

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

flat_land = [height for row in land for height in row]
counter = Counter(flat_land)

min_time = float('inf')
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

print(min_time, max_height)
