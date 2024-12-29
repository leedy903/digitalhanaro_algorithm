import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

n = int(input())
population = [0] + list(map(int, input().split()))

graph = defaultdict(list)
for i in range(n):
    graph[i + 1] = list(map(int, input().split()))[1:]
    
# 지역구를 둘로 나누는 모든 방법에서, 중복 제거
# 가능한 방법의 경우에
# 인구수가 최소로 나눠지는 경우 찾기

check = [False for _ in range(n + 1)]
red_cases = []
def get_red_cases(start, case):
    red_cases.append(case)
    for i in range(start, n + 1):
        if not check[i]:
            check[i] = True
            get_red_cases(i, case + [i])
            check[i] = False

get_red_cases(1, [])

ans = float('inf')
    
for red_case in red_cases:
    visited = [False for _ in range(n + 1)]
    district = [0 for _ in range(n + 1)]
    population_result = []
    
    for red in red_case:
        district[red] = 1

    for i in range(1, n + 1):
        if not visited[i]:
            population_count = population[i]
            visited[i] = True
            color = district[i]
            deq = deque([i])
            while deq:
                cur = deq.popleft()
                for neighbor in graph[cur]:
                    if not visited[neighbor] and district[neighbor] == color:
                        population_count += population[neighbor]
                        visited[neighbor] = True
                        deq.append(neighbor)
            population_result.append(population_count)
    
    if len(population_result) == 2:
        ans = min(ans, abs(population_result[0] - population_result[1]))

ans = ans if ans != float('inf') else -1
print(ans)