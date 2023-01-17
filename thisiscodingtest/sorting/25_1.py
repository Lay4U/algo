from collections import Counter


def solution(n, stages):
    stage_counts = Counter(stages)
    total_player = len(stages)
    fail_rates = []
    for stage in range(1, n + 1):
        if stage in stage_counts:
            fail_rate = stage_counts[stage] / total_player
            total_player -= stage_counts[stage]
            fail_rates.append((stage, fail_rate))
        else:
            fail_rates.append((stage, 0))

    return [stage for stage, _ in sorted(fail_rates, key=lambda x: x[1], reverse=True)]


print(solution(4, [4, 4, 4, 4, 4]))
