n = 8

datas = [4, 3, 6, 8, 7, 5, 2, 1]
stack = []
result = []
count = 1

for data in datas:
    while count <= data:
        stack.append(count)
        result.append('+')
        count += 1

    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('no')
print('\n'.join(result))
