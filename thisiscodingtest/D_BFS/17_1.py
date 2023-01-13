# n, k = map(int, input().split())
# data = []
# for _ in range(n):
#     data.append(list(map(int, input().split())))
# s, x, y = map(int, input().split())
#
# print(n, k)
# print(data)
# print(s, x, y)


n, k = 3, 3
data = [[1, 0, 2], [0, 0, 0], [3, 0, 0]]
s, x, y = 2, 3, 2
# 1번하고, 2번하고, 3번하고 루프를 어떻게?
for k in range(1, k + 1):
    for i in range(n):
        for j in range(n):
            if data[i][j] == k:
                # check left
                if j - 1 >= 0 and data[i][j - 1] == 0:
                    data[i][j - 1] = k
                # check right
                if j + 1 < n and data[i][j + 1] == 0:
                    data[i][j + 1] = k
                # check up
                if i - 1 >= 0 and data[i - 1][j] == 0:
                    data[i - 1][j] = k
                # check down
                if i + 1 < n and data[i + 1][j] == 0:
                    data[i + 1][j] = k
print(data)
