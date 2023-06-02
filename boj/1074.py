def z_order(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n - 1)
    if r < half and c < half:  # 1사분면
        return z_order(n - 1, r, c)
    elif r < half and c >= half:  # 2사분면
        return half ** 2 + z_order(n - 1, r, c - half)
    elif r >= half and c < half:  # 3사분면
        return 2 * half ** 2 + z_order(n - 1, r - half, c)
    else:
        return 3 * half ** 2 + z_order(n - 1, r - half, c - half)


n, r, c = map(int, input().split())
print(z_order(n, r, c))
