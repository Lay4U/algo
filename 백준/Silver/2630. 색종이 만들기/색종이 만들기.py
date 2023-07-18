import sys
input = sys.stdin.readline

def paper(x, y, n):
    global graph, white, blue
    color = graph[x][y]
    half = n // 2
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != color:
                paper(x, y, half)
                paper(x + half, y, half)
                paper(x, y + half, half)
                paper(x + half, y + half, half)
                return
    if color == 0:
        white += 1
    elif color == 1:
        blue += 1


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0
paper(0, 0, n)
print(white)
print(blue)
