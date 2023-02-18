def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a, b = find_parent(parent, a), find_parent(parent, b)
    parent[b] = a if a < b else b if a > b else a


n, m = map(int, input().split())
parent = list(range(n + 1))

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j]:
            union_parent(parent, i + 1, j + 1)

plan = list(map(int, input().split()))

result = all(find_parent(parent, plan[i]) == find_parent(parent, plan[i + 1]) for i in range(m - 1))

print("YES" if result else "NO")
