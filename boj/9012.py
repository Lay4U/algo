T = int(input())
for _ in range(T):
    s = input()

    stack = []
    is_valid = True
    for c in s:
        if c == '(':
            stack.append(c)
        elif not stack:
            is_valid = False
            break
        else:
            stack.pop()
    print('YES' if is_valid and not stack else 'NO')

import sys

vps = sys.stdin.readlines()[1:]

for v in vps:
    v = v.rstrip()
    while '()' in v:
        v = v.replace('()', '')

    if v:
        print('NO')
    else:
        print('YES')
