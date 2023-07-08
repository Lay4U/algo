import sys

input = sys.stdin.readline
n = int(input())
meetings = [(tuple(map(int, input().split()))) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_time = 0

for start, end in meetings:
    if start >= last_time:
        count += 1
        last_time = end

print(count)
