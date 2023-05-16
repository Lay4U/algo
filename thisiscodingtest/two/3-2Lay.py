n, m, k = 5, 8, 3
arr = [2, 4, 5, 4, 6]

arr.sort(reverse=True)
top_k_element = arr[:k]
print(top_k_element)

quotient, remainder = divmod(m, k)
print(quotient, remainder)

total_sum = sum(top_k_element) * quotient + sum(top_k_element[:remainder])

print(total_sum)
