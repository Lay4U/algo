import sys
input = sys.stdin.readline

p = [1, 1, 1]

for i in range(3, 101):
    p.append(p[i - 3] + p[i - 2])

for _ in range(int(input())):
    print(p[int(input()) - 1])
