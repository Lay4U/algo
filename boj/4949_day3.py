pairs = {')': '(', ']': '['}
while True:
    stack = []
    datas = input()
    if datas == '.':
        break
    for data in datas:
        if data == '.':
            print('yes' if not stack else 'no')
            break
        elif data in pairs.values():
            stack.append(data)
        elif data in pairs.keys():
            if stack and stack[-1] == pairs[data]:
                stack.pop()
            else:
                print('no')
                break
