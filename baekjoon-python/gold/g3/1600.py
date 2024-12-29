import sys
from collections import deque
input = sys.stdin.readline

hdy = [-1, -2, -2, -1, 1, 2, 2, 1]
hdx = [-2, -1, 1, 2, 2, 1, -1, -2]
mdy = [-1, 0, 1, 0]
mdx = [0, -1, 0, 1]

k = int(input())
w, h = map(int, input().rstrip().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(h)]
dp = [[[float('inf') for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]

deq = deque([[0, 0, 0]])
for i in range(k + 1):
    dp[0][0][i] = 0

while deq:
    y, x, horse_count = deq.popleft()
    
    if horse_count < k:
        for i in range(8):
            ny = y + hdy[i]
            nx = x + hdx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if matrix[ny][nx] == 0 and dp[ny][nx][horse_count + 1] > dp[y][x][horse_count] + 1:
                    dp[ny][nx][horse_count + 1] = dp[y][x][horse_count] + 1
                    deq.append([ny, nx, horse_count + 1])
                    
    for i in range(4):
        ny = y + mdy[i]
        nx = x + mdx[i]
        if 0 <= ny < h and 0 <= nx < w:
            if matrix[ny][nx] == 0 and dp[ny][nx][horse_count] > dp[y][x][horse_count] + 1:
                dp[ny][nx][horse_count] = dp[y][x][horse_count] + 1
                deq.append([ny, nx, horse_count])

ans = -1 if min(dp[-1][-1]) == float('inf') else min(dp[-1][-1])
print(ans)

