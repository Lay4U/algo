input = """
5 3
1
2
8
4
9
""".strip().split('\n')
n, c = map(int, input[0].split())
array = list(map(int, input[1:]))
array.sort()
print(array)

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1

    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)



