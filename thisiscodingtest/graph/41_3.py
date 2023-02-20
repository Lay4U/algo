def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a, b = find_parent(parent, a), find_parent(parent, b)
    parent[b] = a if a < b else b if b < a else a


n = int(input())
parent = list(range(n + 1))
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j]:
            union(parent, i + 1, j + 1)
