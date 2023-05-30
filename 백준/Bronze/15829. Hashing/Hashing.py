input()
datas = input()
exp = 0
sum = 0
for char in datas:
    base = ord(char) - 96
    sum += base * pow(31, exp)
    exp += 1

print(sum)
