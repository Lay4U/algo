n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]

data.sort(reverse=True)
first, second = data[:2]

quotient, remainder = divmod(m, k + 1)
result = (first * k + second) * quotient + first * remainder
