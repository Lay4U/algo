from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def get_possible(pos, board):
    possible_pos = []
    pos = list(pos)
    p1x, p1y, p2x, p2y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    for i in range(4):
        p1nx, p1ny, p2nx, p2ny = p1x + dx[i], p1y + dy[i], p2x + dx[i], p2y + dy[i]
        if board[p1nx][p1ny] == 0 and board[p2nx][p2ny] == 0:
            possible_pos.append([(p1nx, p1ny), (p2nx, p2ny)])

    if p1x == p2x:
        for i in [-1, 1]:
            if board[p1x + i][p1y] == 0 and board[p2x + i][p2y] == 0:
                possible_pos.append([(p1x, p1y), (p1x + i, p1y)])
                possible_pos.append([(p2x, p2y), (p2x + i, p2y)])

    elif p1y == p2y:
        for i in [-1, 1]:
            if board[p1x][p1y + i] == 0 and board[p2x][p2y + i] == 0:
                possible_pos.append([(p1x, p1y), (p1x, p1y + i)])
                possible_pos.append([(p2x, p2y), (p2x, p2y + i)])

    return possible_pos


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    pos = {(1, 1), (1, 2)}
    visited = []
    queue = deque()

    visited.append(pos)
    queue.append((pos, 0))
    while queue:
        pos, cost = queue.popleft()
        if (n, n) in pos:
            return cost

        for next_pos in get_possible(pos, new_board):
            if next_pos not in visited:
                queue.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
