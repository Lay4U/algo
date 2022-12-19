from itertools import combinations

# 5 2
data = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2],
]

n, m = 5, 2
house, chicken = [], []
for x in range(n):
    for y in range(n):
        if data[x][y] == 1:
            house.append((x, y))
        elif data[x][y] == 2:
            chicken.append((x, y))

print(house)
print(chicken)

candidates = list(combinations(chicken, m))
print(candidates)

result = 0
for hx, hy in house:
    temp = 1e9
    for candidate in candidates:
        for cx, cy in candidate:
            count = min(temp, abs(hx - cx) + abs(hy - cy))
    result += count
print(result)
