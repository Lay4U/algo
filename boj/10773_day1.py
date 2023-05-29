n = int(input())
stack = []

for _ in range(n):
    value = int(input())
    if value == 0:
        stack.pop()
    else:
        stack.append(value)

print(sum(stack))
