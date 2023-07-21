import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    p = input().strip()
    n = int(input())
    datas = input().strip()[1:-1].split(',')
    if n == 0:
        datas = []
    else:
        datas = deque(datas)

    error = False
    reverse = False

    for op in p:
        if op == 'R':
            reverse = not reverse
        elif op == 'D':
            if not datas:
                error = True
                break
            if reverse:
                datas.pop()
            else:
                datas.popleft()

    if error:
        print('error')
    else:
        if reverse:
            datas.reverse()
        print(f"[{','.join(datas)}]")
