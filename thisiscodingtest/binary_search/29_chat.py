import itertools

n, c = map(int, input().split())
data = sorted([int(input()) for _ in range(n)])

diff = [j - i for i, j in zip(data, data[1:])]
print(diff)
groupby = itertools.groupby(diff)
print(groupby)
for k, g in groupby:
    print(k, g)
    for go in g:
        print(go)
result = min(k for k, g in itertools.groupby(diff) if sum(1 for _ in g) >= c - 1)
print(result)

"""
input is
5 3
1
2
8
4
9
"""
