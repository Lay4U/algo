import sys

sys.stdin = open("../input.txt", "rt", encoding="utf-8")

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)
