def possible(result):
    for x, y, stuff in result:
        if stuff == 0:
            if y == 0 or (x - 1, y, 1) in result or (x, y, 1) in result or (x, y - 1, 0) in result:
                continue
            return False
        elif stuff == 1:
            if (x + 1, y - 1, 0) in result or (x, y - 1, 0) in result or \
                    ((x - 1, y, 1) in result and (x + 1, y, 1) in result):
                continue
            return False
    return True


def solution(build_frame, n):
    result = []
    for frame in build_frame:
        x, y, stuff, install = frame

        if install == 0:
            result.remove((x, y, stuff))
            if not possible(result):
                result.append((x, y, stuff))
        elif install == 1:
            result.append((x, y, stuff))
            if not possible(result):
                result.remove((x, y, stuff))
    result.sort()
    return result


print(solution(
    [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]],
    5))
