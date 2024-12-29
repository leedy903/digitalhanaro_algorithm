import sys
from  collections import deque
input = sys.stdin.readline

# 네 방향 움직임
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

# 입력
n, m = map(int, input().rstrip().split())
matrix = [list(map(int, list(input().rstrip()))) for _ in range(n)]

# (0, 0)부터 (n, m)까지 가는 데 걸리는 최단 거리
route = [[float('inf') for _ in range(m)] for _ in range(n)]

# 시작 지점 세팅
deq = deque([[0, 0]])
route[0][0] = 1

# 더 이상 움직일 수 없을 때까지 반복
while deq:
    # 현 위치
    y, x = deq.popleft()
    
    # 현 위치에서 네 방향 탐색
    for i in range(4):
        # 다음 위치
        ny = y + dy[i]
        nx = x + dx[i]
        
        # 정상 범위 확인
        if 0 <= ny < n and 0 <= nx < m:
            # 다음 위치의 값이 1이고, 더 빨리 갈 수 있다면 최단 거리 갱신 및 다음 루트에 추가
            if matrix[ny][nx] == 1 and route[ny][nx] > route[y][x] + 1:
                route[ny][nx] = route[y][x] + 1
                deq.append([ny, nx])

# 출력
print(route[-1][-1])