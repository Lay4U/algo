n = int(input())
m = int(input())
s = input()

count = 0
pattern = 0

i = 1
while i < m - 1:
    if s[i - 1] == "I" and s[i] == "O" and s[i + 1] == "I":
        pattern += 1
        if pattern == n:
            count += 1
            pattern -= 1
        i += 1
    else:
        pattern = 0
    i += 1
print(count)
