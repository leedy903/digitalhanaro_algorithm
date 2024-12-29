import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우 이동
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

# 입력
n, m, t = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]
# 이동한 경로의 최단거리
route = [[float('inf') for _ in range(m)] for _ in range(n)]

# 시작([0, 0]) 지점 deq 및 최단거리 초기화
deq = deque([[0, 0]])
route[0][0] = 0

# BFS 순회
while deq:
    # 현위치
    y, x = deq.popleft()
    
    # 그람을 얻으면 BFS 순회 멈추고 바로 최단거리 갱신
    if matrix[y][x] == 2:
        route[-1][-1] = min(route[-1][-1], route[y][x] + (n - y - 1) + (m - x - 1))
        continue
    
    # 네 방향 탐색
    for i in range(4):
        # 다음 위치
        ny = y + dy[i]
        nx = x + dx[i]
        
        # 좌표 유효성 판단
        if 0 <= nx < m and 0 <= ny < n:
            # 다음 좌표가 벽이 아니고, 더 짧은 거리로 갈 수 있을 경우 진행
            if matrix[ny][nx] != 1 and route[ny][nx] > route[y][x] + 1:
                route[ny][nx] = route[y][x] + 1
                deq.append([ny, nx])

# t 시간 내로 갈 수 있는지 판단
ans = "Fail" if route[-1][-1] > t else route[-1][-1]
print(ans)