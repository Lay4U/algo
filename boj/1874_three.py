# n = 8
# datas = [4, 3, 6, 8, 7, 5, 2, 1]
n = int(input())
datas = [int(input()) for _ in range(n)]
stack = []
answer = []
count = 1
for data in datas:
    while data >= count:
        stack.append(count)
        answer.append('+')
        count += 1
    if stack[-1] == data:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        break
if not stack:
    print('\n'.join(answer))
