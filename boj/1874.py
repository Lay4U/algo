n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1

for num in sequence:
    while current <= num:
        stack.append(current)
        result.append("+")
        current += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        result = ['NO']
        break

print('\n'.join(result))
