from collections import deque


def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1x, pos1y, pos2x, pos2y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1nx, pos1ny, pos2nx, pos2ny = pos1x + dx[i], pos1y + dy[i], pos2x + dx[i], pos2y + dy[i]
        if board[pos1nx][pos1ny] == 0 and board[pos2nx][pos2ny] == 0:
            next_pos.append({(pos1nx, pos1ny), (pos2nx, pos2ny)})
    if pos1x == pos2x:
        for i in [-1, 1]:
            if board[pos1x + i][pos1y] == 0 and board[pos2x + i][pos2y] == 0:
                next_pos.append({(pos1x, pos1y), (pos1x + i, pos1y)})
                next_pos.append({(pos2x, pos2y), (pos2x + i, pos2y)})
    elif pos1y == pos2y:
        for i in [-1, 1]:
            if board[pos1x][pos1y + i] == 0 and board[pos2x][pos2y + i] == 0:
                next_pos.append({(pos1x, pos1y), (pos1x, pos1y + i)})
                next_pos.append({(pos2x, pos2y), (pos2x, pos2y + i)})
    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

    return 0


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
