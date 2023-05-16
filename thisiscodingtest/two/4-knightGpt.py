def knight_moves(position):
    row, col = ord(position[0]) - ord('a') + 1, int(position[1])
    moves = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2)
    ]
    return sum(
        1
        for move in moves
        if 1 <= row + move[0] <= 8 and 1 <= col + move[1] <= 8
    )


position = "a1"
result = knight_moves(position)
print(result)
