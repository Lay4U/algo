import sys
input = sys.stdin.readline
n = int(input())

if n:
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    k = round(n * 0.15 + 0.00000001)
    print(round(sum(arr[k:-k] if k else arr) / (n - 2 * k) + 0.00000001))
else:
    print(0)
