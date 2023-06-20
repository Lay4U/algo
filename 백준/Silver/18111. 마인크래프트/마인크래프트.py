import sys
from collections import Counter

input = sys.stdin.readline

n, m, b = map(int, input().split())
land = [map(int, input().split()) for _ in range(n)]

flat_land = [flat for row in land for flat in row]
counter = Counter(flat_land)
min_time = 1e9
max_height = 0

for h in range(257):
    time = 0
    inventory = b
    for height, depth in counter.items():
        if h > height:
            time += (h - height) * depth
            inventory -= (h - height) * depth
        else:
            time += (height - h) * 2 * depth
            inventory += (height - h) * depth

    if inventory >= 0:
        if min_time >= time:
            min_time = time
            max_height = h

print(min_time, max_height)
