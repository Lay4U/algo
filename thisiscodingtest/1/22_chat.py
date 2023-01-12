from collections import deque


def solution(board):
    n = len(board)
    q = deque([((1, 1), (1, 2)), ])
    visited = set()
    while q:
        pos1, pos2 = q.popleft()
        if pos1 == (n, n) or pos2 == (n, n):
            return cost
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            pos1_next, pos2_next = (pos1[0] + dx, pos1[1] + dy), (pos2[0] + dx, pos2[1] + dy)
            if pos1_next[0] in {0, n + 1} or pos1_next[1] in {0, n + 1} or pos2_next[0] in {0, n + 1} or pos2_next[
                1] in {0, n + 1}:
                continue
            if board[pos1_next[0] - 1][pos1_next[1] - 1] or board[pos2_next[0] - 1][pos2_next[1] - 1]:
                continue
            if (pos1_next, pos2_next) in visited:
                continue
            visited.add((pos1_next, pos2_next))
            q.append((pos1_next, pos2_next))
    return -1


board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print(solution(board))
