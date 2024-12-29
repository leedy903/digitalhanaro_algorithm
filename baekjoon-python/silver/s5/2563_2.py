import sys
input = sys.stdin.readline

length = 100

n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]
prefix = [[0 for _ in range(length + 1)] for _ in range(length + 1)]

for x, y in papers:
    prefix[y - 1][x - 1] += 1
    prefix[y - 1][x + 9] += -1
    prefix[y + 9][x - 1] += -1
    prefix[y + 9][x + 9] += 1
    
for y in range(length):
    for x in range(length):
        prefix[y][x + 1] += prefix[y][x]
        
for y in range(length):
    for x in range(length):
        prefix[y + 1][x] += prefix[y][x]

count = 0
for i in range(length):
    for j in range(length):
        if prefix[i][j] > 0:
            count += 1

print(count)
