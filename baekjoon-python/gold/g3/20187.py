import sys
input = sys.stdin.readline

dx = [1, 0, 3, 2]
dy = [2, 3, 0, 1]

k = int(input())
fold_commands = list(input().split())[::-1]
initial_dot = int(input())
x, y = 1, 1
answer = [[initial_dot]]

for fold in fold_commands:
    unfold_page = [[-1] * x for _ in range(y)]
    for i in range(y):
        for j in range(x):
            if fold in ('L', 'R'):
                unfold_page[i][j] = dx[answer[i][x - j - 1]]
            elif fold in ('U', 'D'):
                unfold_page[i][j] = dy[answer[y - i - 1][j]]
        
    if fold == 'L':
        for i in range(y) :
            answer[i] += unfold_page[i]
        x *= 2
    elif fold == 'R':
        for i in range(y) :
            answer[i] = unfold_page[i] + answer[i]
        x *= 2
    elif fold == 'U':
        answer += unfold_page
        y *= 2
    else:
        answer = unfold_page + answer
        y *= 2
        
for a in answer:
    print(*a)
print()