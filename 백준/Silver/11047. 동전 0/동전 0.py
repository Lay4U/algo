n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

cnt = 0
for coin in coins[::-1]:
    cnt += k // coin
    k %= coin

print(cnt)