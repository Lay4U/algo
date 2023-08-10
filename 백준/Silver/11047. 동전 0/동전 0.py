n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)
count = 0
for coin in coins:
    count += k // coin
    k %= coin
    if k == 0:
        break

print(count)
