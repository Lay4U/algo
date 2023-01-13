from collections import deque


def solution(board):
    n = len(board)
    q = deque([((1, 1), (1, 2)), ])
    visited = set()
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            pos1, pos2 = (pos[0][0] + dx, pos[0][1] + dy), (pos[1][0] + dx, pos[1][1] + dy)
            if pos1[0] in {0, n + 1} or pos1[1] in {0, n + 1} or pos2[0] in {0, n + 1} or pos2[1] in {0, n + 1}:
                continue
            if board[pos1[0] - 1][pos1[1] - 1] or board[pos2[0] - 1][pos2[1] - 1]:
                continue
            if (pos1, pos2) in visited:
                continue
            visited.add((pos1, pos2))
            q.append(((pos1, pos2), cost + 1))
    return -1


board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print(solution(board))
