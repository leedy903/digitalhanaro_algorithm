import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]

dp[0][1] = [1, 0, 0]

for x in range(2, n):
    if matrix[0][x] == 0:
        dp[0][x] = dp[0][x - 1]

for y in range(1, n):
    for x in range(1, n):
        
        if matrix[y][x] == 0:
            dp[y][x][0] = dp[y][x - 1][0] + dp[y][x - 1][2]
            dp[y][x][1] = dp[y - 1][x][1] + dp[y - 1][x][2]
        
            if matrix[y - 1][x] == 0 and matrix[y][x - 1] == 0:
                dp[y][x][2] = sum(dp[y - 1][x - 1])

print(sum(dp[-1][-1]))

