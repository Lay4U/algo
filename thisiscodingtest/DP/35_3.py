input = 10

ugly = [1]
i2, i3, i5 = 0, 0, 0

for _ in range(1, input):
    next_ugly = min(ugly[i2] * 2,
                    ugly[i3] * 3,
                    ugly[i5] * 5)
    ugly.append(next_ugly)
    i2 += next_ugly == ugly[i2] * 2
    i3 += next_ugly == ugly[i3] * 3
    i5 += next_ugly == ugly[i5] * 5

print(ugly)
