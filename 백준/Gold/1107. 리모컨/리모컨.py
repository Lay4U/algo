n = int(input())
m = int(input())
broken_buttons = set(input().split()) if m else set()

answer = abs(n - 100)

for channel in range(1000001):
    for j in range(len(str(channel))):
        if str(channel)[j] in broken_buttons:
            break
    else:
        answer = min(answer, abs(n - channel) + len(str(channel)))
        # print(str(channel)[j], channel, j, answer)

print(answer)
