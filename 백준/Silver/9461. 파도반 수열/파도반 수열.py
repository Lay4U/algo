import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    p = [0, 1, 1, 1]
    for i in range(4, n + 1):
        p.append(p[i - 2] + p[i - 3])
    print(p[n])
