import sys
from collections import deque, defaultdict
input = sys.stdin.readline

# 입력
n = int(input())
target_color = [0] + list(map(int, input().rstrip().split()))
# 인접 리스트
adjacency_list = defaultdict(list)
# 방문 확인 리스트
visited = [False for _ in range(n + 1)]

# 주어진 노드 인접 리스트에 추가
for i in range(n - 1):
    a, b = map(int, input().rstrip().split())
    adjacency_list[a].append(b)
    adjacency_list[b].append(a)

# 0번째 시작 노드로 설정 
adjacency_list[0] = [1]
deq = deque([0])
visited[0] = True

ans = 0

# 트리 순회
while deq:
    cur_node = deq.popleft()
    # 인접 노드 순회
    for next_node in adjacency_list[cur_node]:
        # 아직 방문 하지 않은 노드(자식 노드) 확인
        if not visited[next_node]:
            # 자식 노드와 색이 다르다면 경우의 수 + 1
            if target_color[cur_node] != target_color[next_node]:
                ans += 1
            # 자식 노드 deque에 추가
            deq.append(next_node)
            visited[next_node] = True

print(ans)