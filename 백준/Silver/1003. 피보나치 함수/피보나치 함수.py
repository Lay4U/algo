import sys
input = sys.stdin.readline

def fibo_dp(n):
    fibo_counts = [(1, 0), (0, 1)]

    for i in range(2, n + 1):
        zeros, ones = map(sum, zip(fibo_counts[i - 1], fibo_counts[i - 2]))
        fibo_counts.append((zeros, ones))
    return fibo_counts[n]


T = int(input())
for _ in range(T):
    N = int(input())
    print(*fibo_dp(N))
