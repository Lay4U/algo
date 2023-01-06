from itertools import combinations

input = """
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
""".strip().split('\n')

n = int(input[0])
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input[i + 1].strip().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))


def find_student(x, y, dx, dy):
    while 0 <= x < n and 0 <= y < n:
        if board[x][y] == 'S':
            return True
        if board[x][y] == 'O':
            return False
        x += dx
        y += dy
    return False


def can_see_any_student():
    for x, y in teachers:
        if any(find_student(x, y, dx, dy) for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0))):
            return True
        return False


find = False

for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'
    if not can_see_any_student():
        find = True
        break
    for x, y in data:
        board[x][y] = 'X'

print('YES' if find else 'No')
