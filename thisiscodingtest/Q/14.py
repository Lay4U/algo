from itertools import permutations


def solution(n, weak, dist):
    for i in weak:
        weak.append(weak[i] + n)

    length = len(weak)

    answer = len(dist) + 1

    for start in range(length):
        for friend in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friend[count - 1]
            for index in (start, start + length):
                if position < weak[start]:
                    count += 1
                    if count > len(dist):
                        break
            answer = min(answer, count)

    if answer > len(dist):
        return -1
    return answer
