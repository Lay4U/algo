n = int(input())
datas = list(int(input()) for i in range(n))

count = 1
stack = []
answer = []
for data in datas:
    while count <= data:
        stack.append(count)
        answer.append('+')
        count += 1
    if stack and stack[-1] == data:
        stack.pop()
        answer.append('-')
    else:
        answer = ['NO']
        break

print('\n'.join(answer))
