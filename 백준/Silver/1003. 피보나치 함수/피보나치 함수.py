import sys

input = sys.stdin.readline
fibo_counts = [(1, 0), (0, 1)]
for i in range(2, 50):
    ones, zeros = map(sum, zip(fibo_counts[i - 1], fibo_counts[i - 2]))
    fibo_counts.append((ones, zeros))
    # print(i, ones, zeros, '\t', fibo_counts)

T = int(input())
for _ in range(T):
    n = int(input())
    print(*fibo_counts[n])
