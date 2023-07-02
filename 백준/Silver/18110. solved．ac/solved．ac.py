import sys

input = sys.stdin.readline


def my_round(value):
    return int(value) + 1 if value - int(value) >= 0.5 else int(value)


n = int(input())
if n == 0:
    print(0)
    exit()
datas = [int(input()) for _ in range(n)]
datas.sort()
k = my_round(len(datas) * 0.15)
datas = datas[k:-k] if k else datas
print(my_round(sum(datas) / len(datas)))
