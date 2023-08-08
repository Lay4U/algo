from collections import defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    clothes = defaultdict(int)
    for _ in range(int(input())):
        name, category = input().split()
        clothes[category] += 1
    count = 1
    for category, value in clothes.items():
        count = count * (value + 1)
    print(count - 1)
