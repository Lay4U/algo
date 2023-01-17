from collections import Counter


def solution(n, stages):
    stage_list = Counter(stages)
    fail_list = []
    print(stage_list)
    count = len(stages)
    for stage in range(1, n + 1):
        if stage in stage_list:
            failure = stage_list[stage] / count
            count -= stage_list[stage]
            fail_list.append((stage, failure))
            print(count)
        else:
            fail_list.append((stage, 0))
    print(fail_list)
    # return [x for x in fail_list.sort(key=lambda x: x[1], reverse=True)[0]]
    # return [stage for stage, _ in sorted(fail_list, key=lambda x: x[1], reverse=True)]
    fail_list.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in fail_list]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
