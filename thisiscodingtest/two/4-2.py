def count_cases_with_3(n):
    count = 0
    for h in range(n + 1):
        for m in range(60):
            for s in range(60):
                if '3' in f'{h:02}{m:02}{s:02}':
                    count += 1
    return count


n = 5
result = count_cases_with_3(n)
print(result)
