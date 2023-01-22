from bisect import bisect_left, bisect_right
from collections import defaultdict


def count_by_range(array, left, right):
    left_index = bisect_left(array, left)
    right_index = bisect_right(array, right)
    return right_index - left_index


def solution(words, queries):
    array = defaultdict(list)
    reversed_array = defaultdict(list)

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for k in array.keys():
        array[k].sort()
        reversed_array[k].sort()

    result = []
    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)],
                                 q.replace('?', 'a'),
                                 q.replace('?', 'z'))
        else:
            res = count_by_range(reversed_array[len(q)],
                                 q[::-1].replace('?', 'a'),
                                 q[::-1].replace('?', 'z'))
        result.append(res)
    return result


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
