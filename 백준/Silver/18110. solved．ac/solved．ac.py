import sys
from collections import deque

num = int(sys.stdin.readline())
except_num = round(num * 0.15 + 0.00000001)
result = 0
data = deque()

if num == 0:
    print(0)
    exit()

for _ in range(num):
    data.append(int(sys.stdin.readline()))

data = deque(sorted(data))

for _ in range(except_num):
    data.popleft()
    data.pop()

for i in data:
    result += i

result = round(result / len(data) + 0.0000001)
print(result)