pairs = {')': '(', ']': '['}

while True:
    stack = []
    datas = input()
    if datas == '.':
        break
    balanced = True
    for char in datas:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                balanced = False
                break
    print('yes' if balanced and not stack else 'no')

