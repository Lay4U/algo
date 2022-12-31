import sys

sys.stdin = open("../input.txt", "rt", encoding="utf-8")

# 3 4
n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0

print(array)
for i in range(n):
    for j in range(array[i], m + 1):
        print('###', j)
        if d[j - array[i]] != 10001:
            print()
            print('asdf', d[j])
            d[j] = min(d[j], d[j - array[i]] + 1)
            print(d[j])
            print()

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

print()
for i in range(len(d)):
    print(i, d[i])
