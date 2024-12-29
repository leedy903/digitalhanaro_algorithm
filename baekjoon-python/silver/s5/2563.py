import sys
input = sys.stdin.readline

n = int(input())
matrix = [[False for _ in range(100)] for _ in range(100)]
papers = [list(map(int, input().split())) for _ in range(n)]

for y, x in papers:
    for i in range(10):
        for j in range(10):
            matrix[y + i][x + j] = True
            
count = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j] == True:
            count += 1

print(count)