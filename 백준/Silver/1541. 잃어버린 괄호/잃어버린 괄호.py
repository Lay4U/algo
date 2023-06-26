expression = input().split('-')
result = sum(map(int, expression[0].split('+')))
for exp in expression[1:]:
    result -= sum(map(int, exp.split('+')))
print(result)
