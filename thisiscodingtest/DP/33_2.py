input = """
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
""".strip().split('\n')

n = int(input[0])

t = []
p = []

for i in range(1, n + 1):
    a, b = map(int, input[i].split())
    t.append(a)
    p.append(b)

dp = [0] * (n + 1)
max_value = 0
for i in range(n - 1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)
