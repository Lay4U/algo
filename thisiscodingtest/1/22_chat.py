from collections import deque


def get_next_pos(pos, board):
    next_pos = []
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        x1_next, y1_next, x2_next, y2_next = x1 + dx, y1 + dy, x2 + dx, y2 + dy
        if board[x1_next][y1_next] == 0 and board[x2_next][y2_next] == 0:
            next_pos.append([(x1_next, y1_next), (x2_next, y2_next)])
    if x1 == x2:
        for i in [-1, 1]:
            if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                next_pos.append([(x1, y1), (x1 + i, y1)])
                next_pos.append([(x2, y2), (x2 + i, y2)])
    elif y1 == y2:
        for i in [-1, 1]:
            if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                next_pos.append([(x1, y1), (x1, y1 + i)])
                next_pos.append([(x2, y2), (x2, y2 + i)])
    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    queue = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    queue.append((pos, 0))
    visited.append(pos)
    while queue:
        pos, cost = queue.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                queue.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
