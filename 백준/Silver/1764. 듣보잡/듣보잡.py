import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = {input().strip() for _ in range(n)}
b = {input().strip() for _ in range(n)}

result = sorted(a & b)
print(len(result))
for name in result:
    print(name)
