import sys

input = sys.stdin.readline
datas = [int(input()) for _ in range(int(input()))]
stack = []
[stack.pop() if data == 0 else stack.append(data) for data in datas]
print(sum(stack))
