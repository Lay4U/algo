n = 5
plan = "R R R U D D"

position = (1, 1)
for direction in plan.split():
    x, y = position
    dx, dy = {
        "L": (-1, 0),
        "R": (1, 0),
        "U": (0, -1),
        "D": (0, 1)
    }[direction]
    nx, ny = x + dx, y + dy
    position = (max(1, min(n, nx)), max(1, min(n, ny)))

print(position)
