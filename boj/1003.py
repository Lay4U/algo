"""
0 -> f(0) -> 1 0
1 -> f(1) -> 0 1
2 -> f(2) -> f(1) + f(0) -> 1 1
3 -> f(3) -> f(2) + f(1) -> 1 2

f(0) -> 1 0
f(1) -> 0 1
f(2) -> 1 1
f(3) -> 1 2
f(4)
"""

n = 6


def f(n):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)
    else:
        return f(n - 1) + f(n - 2)

f = []
f.append((1, 0))
f.append((0, 1))
result = ()
for i in range(n):
    if i == 0:
        result = (1, 0)
    elif i == 1:
        result = (0, 1)
    else:
        if not f[i]:
            f[i] = f[i-1] + f[i-2]
        else:


