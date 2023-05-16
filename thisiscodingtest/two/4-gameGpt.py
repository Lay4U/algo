def move_character(N, M, A, B, d, grid):
    visited = set()
    direction = ((-1, 0), (0, 1), (1, 0), (0, -1))

    def is_valid_move(x, y):
        return 0 <= x < N and 0 <= y < M and grid[x][y] == 0

    while True:
        visited.add((A, B))

        for _ in range(4):
            d = (d - 1) % 4
            next_A, next_B = A + direction[d][0], B + direction[d][1]

            if is_valid_move(next_A, next_B) and (next_A, next_B) not in visited:
                A, B = next_A, next_B
                break
        else:
            A -= direction[d][0]
            B -= direction[d][1]

            if not is_valid_move(A, B):
                break

    return len(visited)
