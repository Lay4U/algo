n = 5
data = ['R', 'R', 'R', 'U', 'D', 'D']

result = [1, 1]

for x in data:
    if x == 'R' and result[1] + 1 < n:
        result[1] += 1
    elif x == 'L' and result[1] - 1 > 0:
        result[1] -= 1
    elif x == 'D' and result[0] + 1 < n:
        result[0] += 1
    elif x == 'U' and result[0] - 1 > 0:
        result[0] -= 1

print(result)
