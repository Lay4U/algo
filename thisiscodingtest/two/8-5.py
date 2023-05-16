x = 26
d = [0] * 99999

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    print(f"\ni = {i}, Initial value (subtract 1): d[{i}] = {d[i]}")

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
        print(f"i = {i}, Check division by 2: d[{i // 2}] = {d[i // 2]}, d[{i}] updated to {d[i]}")

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
        print(f"i = {i}, Check division by 3: d[{i // 3}] = {d[i // 3]}, d[{i}] updated to {d[i]}")

    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
        print(f"i = {i}, Check division by 5: d[{i // 5}] = {d[i // 5]}, d[{i}] updated to {d[i]}")

    print(f"After processing i = {i}, d[2:{i + 1}] = {d[2:i + 1]}")

print("\nResult:", d[x])
