n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))

last_end = 0
count = 0
for start, end in meetings:
    if start >= last_end:
        count += 1
        last_end = end

print(count)
