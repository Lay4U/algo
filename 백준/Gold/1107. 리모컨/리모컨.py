n = int(input())
m = int(input())
broken = set(input()) if m else set()

answer = abs(n - 100)

for channel in range(1000001):
    for j in range(len(str(channel))):
        if str(channel)[j] in broken:
            break
    else:
        answer = min(answer, abs(channel - n) + len(str(channel)))

print(answer)
