def count_paper(x, y, n):
    global paper, white, blue
    color = paper[x][y]
    half = n // 2

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                count_paper(x, y, half)
                count_paper(x + half, y, half)
                count_paper(x, y + half, half)
                count_paper(x + half, y + half, half)
                return

    if color == 0:
        white += 1
    else:
        blue += 1


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white, blue = 0, 0
count_paper(0, 0, n)
print(white)
print(blue)
