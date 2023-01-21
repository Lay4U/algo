from collections import Counter


def solution(n, stage):
    state_counts = Counter(stage)
    total_players = len(stage)
    failure_rate = []

    for stage in range(1, n + 1):
        if stage in state_counts:
            failure = state_counts[stage] / total_players
            total_players -= state_counts[stage]
            failure_rate.append((stage, failure))
        else:
            failure_rate.append((stage, 0))

    return [result for result, _ in sorted(failure_rate, key=lambda x: x[1], reverse=True)]


print(solution(5, [2, 1, 2, 6, 4, 3, 3]))
