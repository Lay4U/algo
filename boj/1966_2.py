n, m = 4, 2
data = [1, 2, 3, 4]

count = 0
for index, value in enumerate(data):
    if value:
        print(index, value)
    count += 1
print(count)
