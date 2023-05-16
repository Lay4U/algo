def josephus(n, k):
    people = list(range(1, n + 1))
    index = 0
    result = []
    while people:
        index = (index + k - 1) % len(people)
        print(index)
        result.append(people.pop(index))
    return result


n, k = map(int, input().split())
print('<' + ', '.join(map(str, josephus(n, k))) + '>')
