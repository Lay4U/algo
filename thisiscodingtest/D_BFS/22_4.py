from collections import deque


def possible(pos, board):
    position = []
    pos = list(pos)
    p1x, p1y, p2x, p2y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        p1nx = p1x + dx[i]
        p1ny = p1y + dy[i]
        p2nx = p2x + dx[i]
        p2ny = p2y + dy[i]
        if board[p1nx][p1ny] == 0 and board[p2nx][p2nx] == 0:
            position.append([(p1nx, p1ny), (p2nx, p2ny)])

    if p1x == p2x:
        for i in [-1, 1]:
            if board[p1x + i][p1y] == 0 and board[p2x + i][p2y] == 0:
                position.append([(p1x, p1y), (p1x + i, p1y)])
                position.append([(p2x, p2y), (p2x + i, p2y)])

    elif p1y == p2y:
        for i in [-1, 1]:
            if board[p1x][p2y + i] == 0 and board[p2x][p2y + i] == 0:
                position.append([(p1x, p1y), (p1x, p1y + i)])
                position.append([(p2x, p2y), (p2x, p2y + i)])

    return position


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    pos = {(1, 1), (1, 2)}
    queue = deque()
    queue.append((pos, 0))
    visited = []
    visited.append(pos)

    while queue:
        pos, cost = queue.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in possible(pos, new_board):
            if next_pos not in visited:
                queue.append((next_pos, cost + 1))
                visited.append(pos)


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
