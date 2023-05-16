from collections import Counter

# N = 10
# data1 = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
# M = 8
# data2 = [10, 9, -5, 2, 3, 4, 5, -10]

N = int(input())
data1 = map(int, input().split())
M = int(input())
data2 = map(int, input().split())

result = Counter(data1)

for i in data2:
    print(result.get(i) if result.get(i) else 0, end=' ')
