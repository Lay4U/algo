import sys

input = sys.stdin.readline

n, m = map(int, input().split())
not_heard = {input().strip() for _ in range(n)}
not_seen = {input().strip() for _ in range(n)}
both = sorted(list(not_heard & not_seen))

print(len(both))
for name in both:
    print(name)
