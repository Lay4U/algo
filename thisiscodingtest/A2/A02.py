import sys

sys.stdin = open("../input.txt", "rt", encoding="utf-8")

# data = list(map(int, input()))
#
# result = 0
#
# for i in range(len(data)):
#     if data[i] == 1 or data[i] == 0:
#         result += data[i]
#     else:
#         result *= data[i]
#
# print(result)

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
