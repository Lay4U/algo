def count_cases_with_3(n):
    return sum("3" in f"{h:02}{m:02}{s:02}" for h in range(n + 1) for m in range(60) for s in range(60))


n = 5
result = count_cases_with_3(n)
print(result)
