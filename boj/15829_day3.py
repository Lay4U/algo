import sys

input = sys.stdin.readline

n = int(input())
datas = input().strip()
# n = 5
# datas = 'abcde'
result = 0
exp = 0
for data in datas:
    # print(data)
    ai = ord(data) - ord('a') + 1
    result += ai * pow(31, exp)
    exp += 1
    # print(ai, exp - 1)
result %= 1234567891
print(result)
