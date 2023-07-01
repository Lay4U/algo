def factorial(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum


n = int(input())
value = str(factorial(n))
result = 0
for char in value[::-1]:
    if char == '0':
        result += 1
    else:
        break
print(result)
