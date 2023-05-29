# pairs = {')': '(', ']': '['}
#
# while True:
#     stack = []
#     datas = input()
#     if datas == '.':
#         break
#     for char in datas:
#         if char == '.':
#             if not stack:
#                 print('yes')
#             else:
#                 print('no')
#
#         elif char in '([':
#             stack.append(char)
#
#         elif char in ')]':
#             if not stack or stack[-1] != pairs[char]:
#                 print('no')
#                 break
#             else:
#                 stack.pop()

pairs = {')': '(', ']': '['}

while True:
    stack = []
    datas = input()
    if datas == '.':
        break
    for char in datas:
        if char == '.':
            print('yes' if not stack else 'no')
        elif char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack[-1] != pairs[char]:
                print('no')
                break
            stack.pop()
