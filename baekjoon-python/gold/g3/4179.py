import sys
from collections import deque
input = sys.stdin.readline

impossible = "IMPOSSIBLE"

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

r, c = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(r)]

j_visit = [[float('inf') for _ in range(c)] for _ in range(r)]
f_visit = [[float('inf') for _ in range(c)] for _ in range(r)]
j_deq = deque([])
f_deq = deque([])

for i in range(r):
    for j in range(c):
        if matrix[i][j] == "J":
            j_visit[i][j] = 1
            j_deq.append([i, j])
        elif matrix[i][j] == "F":
            f_visit[i][j] = 1
            f_deq.append([i, j])

ans = float('inf')

# 불 이동
def f_bfs():
    while f_deq:
        fy, fx = f_deq.popleft()
        for i in range(4):
            nfy = fy + dy[i]
            nfx = fx + dx[i]
            if 0 <= nfy < r and 0 <= nfx < c:
                if matrix[nfy][nfx] != "#" and f_visit[nfy][nfx] == float('inf'):
                    f_visit[nfy][nfx] = f_visit[fy][fx] + 1
                    f_deq.append([nfy, nfx])


def j_bfs():
    # 불 이동한 곳을 더 빨리 갈 수 있으면 생존
    while j_deq:
        jy, jx = j_deq.popleft();
        for i in range(4):
            njy = jy + dy[i]
            njx = jx + dx[i]
            if not (0 <= njy < r and 0 <= njx < c):
                if f_visit[jy][jx] > j_visit[jy][jx]:
                    return j_visit[jy][jx]
            if 0 <= njy < r and 0 <= njx < c:
                if f_visit[njy][njx] <= j_visit[jy][jx] + 1:
                    continue
                if matrix[njy][njx] != "#" and j_visit[njy][njx] == float('inf'):
                    j_visit[njy][njx] = j_visit[jy][jx] + 1
                    j_deq.append([njy, njx])
    return -1

f_bfs()
ans = j_bfs()
if ans == -1:
    ans = impossible
print(ans)

for i in range(r):
    for j in range(c):
        print(f_visit[i][j], end = " ")
    print()
print()

for i in range(r):
    for j in range(c):
        print(j_visit[i][j], end = " ")
    print()
print()

