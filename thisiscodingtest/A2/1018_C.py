arr = []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1], reverse=True)
arr.sort(key=lambda x: x[0])

print(arr)
