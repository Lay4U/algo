# k = int(input())
# stack = []
# for _ in range(k):
#     value = int(input())
#     if value == 0:
#         stack.pop()
#     else:
#         stack.append(value)
# print(sum(stack))

k = int(input())
stack = []
stack = [stack.append(int(input())) or stack.pop() if stack and stack[-1] == 0 else None for _ in range(k)]
print(stack)
