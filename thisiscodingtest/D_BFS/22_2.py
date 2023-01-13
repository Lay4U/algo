from collections import deque


def get_possible_position(pos, board):
    possible_moves = []
    pos = list(pos)
    p1x, p1y, p2x, p2y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1nx, pos1ny, pos2nx, pos2ny = p1x + dx[i], p1y + dy[i], p2x + dx[i], p2y + dy[i]
        if board[pos1nx][pos1ny] == 0 and board[pos2nx][pos2ny] == 0:
            possible_moves.append([(pos1nx, pos1ny), (pos2nx, pos2ny)])
    if p1x == p2x:
        for i in [-1, 1]:
            if board[p1x + i][p1y] == 0 and board[p2x + i][p2y] == 0:
                possible_moves.append([(p1x, p1y), (p1x + i, p1y)])
                possible_moves.append([(p2x, p2y), (p2x + i, p2y)])
    elif p1y == p2y:
        for i in [-1, 1]:
            if board[p1x][p1y + i] == 0 and board[p2x][p2y + i] == 0:
                possible_moves.append([(p1x, p1y), (p1x, p1y + i)])
                possible_moves.append([(p2x, p2y), (p2x, p2y + i)])
    print(possible_moves)
    return possible_moves


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
        for next_pos in get_possible_position(pos, new_board):
            if next_pos not in visited:
                visited.append(next_pos)
                q.append((next_pos, cost + 1))
    return 0


# print(0)
print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
