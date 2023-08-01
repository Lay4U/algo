from collections import defaultdict

for _ in range(int(input())):
    cloth = defaultdict(int)
    for _ in range(int(input())):
        item, category = input().split()
        cloth[category] += 1
    result = 1
    for key in cloth.keys():
        result *= (cloth[key] + 1)
    print(result - 1)
