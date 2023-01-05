# Read in the size of the board
from itertools import combinations

n = int(input())

# Initialize the board, teachers, and spaces lists
board = []
teachers = []
spaces = []

# Read in the board and populate the teachers and spaces lists
for i in range(n):
    row = input().split()
    board.append(row)
    for j, element in enumerate(row):
        if element == 'T':
            teachers.append((i, j))
        elif element == 'X':
            spaces.append((i, j))


def can_see_student(x, y, dx, dy):
    """
    Returns True if the teacher at (x, y) can see a student
    in the direction (dx, dy), and False otherwise.
    """
    while 0 <= x < n and 0 <= y < n:
        if board[x][y] == 'S':
            return True
        if board[x][y] == 'O':
            return False
        x += dx
        y += dy
    return False


def can_see_any_student():
    """
    Returns True if any teacher can see a student, and False otherwise.
    """
    for x, y in teachers:
        for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):  # Check in all four directions
            if can_see_student(x, y, dx, dy):
                return True
            else:
                return False


# Try all combinations of three spaces to block
for combo in combinations(spaces, 3):
    # Block the spaces in the combo
    for x, y in combo:
        board[x][y] = 'O'
    # Check if any teacher can see a student
    if not can_see_any_student():
        print("YES")
        exit()
    # Unblock the spaces
    for x, y in combo:
        board[x][y] = 'X'
print('NO')
