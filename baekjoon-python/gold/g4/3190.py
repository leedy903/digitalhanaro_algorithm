import sys
from  collections import deque
input = sys.stdin.readline

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

n = int(input())
k = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
commands = deque([])

for i in range(k):
    y, x = map(int, input().rstrip().split())
    matrix[y - 1][x - 1] = 1
    
l = int(input())
for i in range(l):
    time, turn = input().split()
    commands.append([int(time), turn])

snake = deque([[0, 0]])
direction = 2
playTime = 0
while True:
    hy, hx = snake[0]
    if commands and commands[0][0] == playTime:
        _, turn = commands.popleft()
        if turn == "L":
            direction = (direction - 1) % 4
        elif turn == "D":
            direction = (direction + 1) % 4
    
    ny = hy + dy[direction]
    nx = hx + dx[direction]
    
    playTime += 1    
    
    if 0 <= ny < n and 0 <= nx < n and [ny, nx] not in snake:
        snake.appendleft([ny, nx])
        if matrix[ny][nx] == 0:
            snake.pop()
        elif matrix[ny][nx] == 1:
            matrix[ny][nx] = 0
    else:
        break

print(playTime)