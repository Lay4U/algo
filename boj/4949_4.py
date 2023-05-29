pairs = {')': '(', ']': '['}
while True:
    stack = []
    datas = input()
    if datas == '.':
        break
    for char in datas:
        if char == '.' and not stack:
            print('yes')
            break
        if char == '.' and stack:
            print('no')
            break
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                print('no')
                break
