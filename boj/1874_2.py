n = int(input())
sequence = [int(input()) for _ in range(n)]
stack = []
output = []
current = 1

for num in sequence:
    while current <= num:
        stack.append(current)
        output.append('+')
        current += 1
    if stack[-1] == num:
        stack.pop()
        output.append('-')
    else:
        print('NO')
        break
    print(num, stack)
else:
    print('\n'.join(output))
# while data:
#     pop = data.pop(0)
#     for i in range(1, pop + 1):
#         if not stack:
#             stack.append(i)
#         elif stack[-1] < i:
#             stack.append(i)
#
#     if stack[-1] > pop:
#         print('No')
#         break
#     elif stack[-1] == pop:
#         stack.pop()
#     print(stack, pop)
