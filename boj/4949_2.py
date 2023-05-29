datas = 'So when I die (the [first] I will see in (heaven) is a score list).'

stack = []
pairs = {')': '(', ']': '['}
for char in datas:
    if char == '.':
        if not stack:
            print('yes')
        break

    if char in '([':
        stack.append(char)
    elif char in ')]':
        if not stack or stack[-1] != pairs[char]:
            print('no')
        else:
            stack.pop()
