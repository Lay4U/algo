'''
1,2,3,4,5,6,7
3(2)
124567
6(4)
12457
2(1)
1457
7(3)
145
5(2)
14
4(1)
1
1(0)

0 ~ length
'''
N = 7
K = 3
data = [i for i in range(1, N + 1)]
index = 0
result = []
while data:
    print(index, index + K - 1, len(data))
    index = (index + K - 1) % len(data)
    result.append(data.pop(index))

print(result)
