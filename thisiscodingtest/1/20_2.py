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

print(board)
print(teachers)
print(spaces)


def find_student(x, y, direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
        return False

    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
        return False

    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
        return False

    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
        return False


def process():
    for x, y in teachers:
        for i in range(4):
            if find_student(x, y, i):
                return True
    return False


find = False

for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'
    if not process():
        find = True
        break
    for x, y in data:
        board[x][y] = 'X'

print('YES' if find == True else 'No')
