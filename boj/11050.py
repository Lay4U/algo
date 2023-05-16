N, K = map(int, input().split())
fact = [1] * 100

for i in range(1, 100):
    fact[i] = fact[i - 1] * i

print(fact[N] // (fact[K] * fact[N - K]))
