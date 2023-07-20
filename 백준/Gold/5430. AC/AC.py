from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    x = input().rstrip()[1:-1].split(',')
    if n == 0:
        x = []
    else:
        x = deque(x)
    error = False
    reverse = False
    for op in p:
        if op == 'R':
            reverse = not reverse
        elif op == 'D':
            if not x:
                error = True
                break
            if reverse:
                x.pop()
            else:
                x.popleft()
    if error:
        print('error')
    else:
        if reverse:
            x.reverse()
        print(f"[{','.join(x)}]")