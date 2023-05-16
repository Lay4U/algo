n, k = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse=True)

result = sum(
    [
        b[i]
        if i < k and a[i] < b[i]
        else a[i]
        for i in range(n)
    ]
)
print(result)
