import sys

input = sys.stdin.readline
n = int(input())
datas = [int(input()) for _ in range(n)]

stack = []
for data in datas:
    stack.pop() if data else stack.append(data)

print(0 if not stack else sum(stack))
