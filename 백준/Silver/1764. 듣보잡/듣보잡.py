import sys

input = sys.stdin.readline

n, m = map(int, input().split())

n = {input().strip() for _ in range(n)}
m = {input().strip() for _ in range(m)}

result = sorted(n & m)
print(len(result))
for name in result:
    print(name)
