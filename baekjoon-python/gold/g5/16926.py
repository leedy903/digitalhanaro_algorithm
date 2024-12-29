import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우 이동
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 입력
n, m, r = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]

# depth: 전체 배열의 깊이
# 폭과 높이 중 작은 것을 depth로 이용
depth = min(n, m) // 2

# 전체 배열을 껍질 단위로 밖에서부터 안쪽으로 순회
for d in range(depth):
    # ㅁ 모양의 껍질에 해당하는 배열의 값을 순서대로 가지는 deque
    deq = deque()
    # 시작 위치 설정
    y, x = d, d
    # 4 방향 순회
    for i in range(4):
        # 한 방향으로 갈 수 있는 최대까지 deq에 추가(복사)
        while True:
            ny = y + dy[i]
            nx = x + dx[i]
            # 좌표 유효성 판단
            if d <= ny < n - d and d <= nx < m - d:
                deq.append(matrix[ny][nx])
                y, x = ny, nx
            else:
                break
    
    # deq을 r % 배열의 길이만큼 반시계 방향 회전
    deq.rotate(-r % ((n + m - 4 * d) * 2 - 4))
    
    # 다시 시작 위치 설정
    y, x = d, d
    # 4방향 순회
    for i in range(4):
        # 한 방향으로 갈 수 있는 최대까지 deq에 있는 값을 matrix에 붙여넣기
        while True:
            ny = y + dy[i]
            nx = x + dx[i]
            # 좌표 유효성 판단
            if d <= ny < n - d and d <= nx < m - d:
                matrix[ny][nx] = deq.popleft()
                y, x = ny, nx
            else:
                break

# 출력
for row in matrix:
    print(*row)