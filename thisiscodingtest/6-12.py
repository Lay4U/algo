import sys

sys.stdin = open("input.txt", "rt", encoding="utf-8")

n, k = map(int, input().split())
print(n, k)
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(a, b)

a.sort()
b.sort(reverse=True)

print(a)
print(b)
print()
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(a)
print(b)
print(sum(a))
