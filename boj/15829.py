# l = int(input())
# string = input()
#
# result = 0
# for i in range(l):
#     result += (ord(string[i]) - 96) * pow(31, i)
# print(result // 123456789)

input()
datas = input()
exp = 0
sum = 0
for char in datas:
    base = ord(char) - 96
    sum += base * pow(31, exp)
    exp += 1
print(sum % 1234567891)
