def zindex(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n - 1)

    if r < half:
        if c < half:
            return zindex(n - 1, r, c)
        else:
            return half ** 2 + zindex(n - 1, r, c - half)
    else:
        if c < half:
            return 2 * half ** 2 + zindex(n - 1, r - half, c)
        else:
            return 3 * half ** 2 + zindex(n - 1, r - half, c - half)


n, r, c = map(int, input().split())
print(zindex(n, r, c))
