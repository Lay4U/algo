from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    datas = defaultdict(int)
    for _ in range(n):
        name, category = input().strip().split()
        datas[category] += 1

    result = 1
    for category, count in datas.items():
        result *= count + 1

    print(result - 1)
