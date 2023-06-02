import sys

input = sys.stdin.readline
fibo = [(1, 0), (0, 1)]

for i in range(2, 51):
    ones, zeros = map(sum, zip(fibo[i - 1], fibo[i - 2]))
    fibo.append((ones, zeros))

T = int(input())

for _ in range(T):
    print(*(fibo[int(input())]))
