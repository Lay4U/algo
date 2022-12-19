import sys

sys.stdin = open("../input.txt", "rt", encoding="utf-8")

n = int(input())

array = list(map(int, input().split()))

array.sort()

result = 0
count = 0

for x in array:
    count += 1
    if count >= x:
        result += 1
        count = 0

print(result)
