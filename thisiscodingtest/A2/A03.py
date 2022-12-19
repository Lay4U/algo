a, b = map(int, input().split())
result = 0
temp = []
for i in range(a):
    temp.append(input())
countWB = [x.count('WB') for x in temp]
countBW = [x.count('BW') for x in temp]
print(countWB)
print(countBW)
maxWB = 0
maxBW = 0
for i in range(a - 8 + 1):
    maxWB = max(maxWB, sum(countWB[i:7 + i]))
    maxBW = max(maxBW, sum(countBW[i:7 + i]))
print(maxWB)
print(maxBW)
