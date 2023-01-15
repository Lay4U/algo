from collections import Counter


def solution(N, stages):
    stage_counts = Counter(stages)
    total_players = len(stages)
    fail_rates = []
    for stage in range(1, N + 1):
        if stage in stage_counts:
            fail_rate = stage_counts[stage] / total_players
            total_players -= stage_counts[stage]
            fail_rates.append((stage, fail_rate))
        else:
            fail_rates.append((stage, 0))

    return [stage for stage, _ in sorted(fail_rates, key=lambda x: x[1], reverse=True)]