from math import gcd

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    lcm = m * n // gcd(m, n)
    result = -1
    for i in range(x, lcm + 1, m):
        if (i - y) % n == 0:
            result = i
            break
    print(result)
