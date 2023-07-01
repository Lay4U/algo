import sys

input = sys.stdin.readline
n = int(input())

def custom_round(n):
    return int(n) + 1 if n - int(n) >= 0.5 else int(n)

if n:
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    k = custom_round(n * 0.15)
    print(custom_round(sum(arr[k:-k] if k else arr) / (n - 2 * k)))
else:
    print(0)
