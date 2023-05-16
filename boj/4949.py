def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '['}

    for char in s:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if not stack or stack[-1] != pairs[char]:
                return 'no'
            stack.pop()
    return 'yes' if not stack else 'no'


while True:
    string = input().strip()
    if string == '.':
        break
    print(is_balanced(string))
