'''
1, 0
0, 1
1, 1
1, 2
'''


def fibo(n):
    fibo_counts = [(1, 0), (0, 1)]
    for i in range(2, n + 1):
        zeros = fibo_counts[i - 1][0] + fibo_counts[i - 2][0]
        ones = fibo_counts[i - 1][1] + fibo_counts[i - 2][1]
        fibo_counts.append((zeros, ones))
        print(fibo_counts)


def fibo2(n):
    fibo_counts = [(1, 0), (0, 1)]

    for i in range(2, n + 1):
        zeros, ones = map(sum, zip(fibo_counts[i - 1], fibo_counts[i - 2]))
        fibo_counts.append((zeros, ones))
        # print(i, zeros, ones, '\t', fibo_counts)

    return fibo_counts[n]


# fibo(5)
# print()
for _ in range(int(input())):
    print(*fibo2(int(input())))
