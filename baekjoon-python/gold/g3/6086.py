import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

def to_num(alpha):
    return ord(alpha) - ord('A')


def find_min(node):
    global min_flow
    if node == 0:
        return
    
    rest = capacity[prev[node]][node] - flow[prev[node]][node]
    min_flow = min(rest, min_flow)
    find_min(prev[node])
    
    
def make_flow(node):
    if node == 0:
        return
    
    flow[prev[node]][node] += min_flow
    flow[node][prev[node]] -= min_flow
    
    make_flow(prev[node])

node_len = 52
fin = to_num('Z')
total_flow = 0

n = int(input())
graph = defaultdict(list)
capacity = [[0 for _ in range(node_len)] for _ in range(node_len)]
flow = [[0 for _ in range(node_len)] for _ in range(node_len)]

for i in range(n):
    u, v, w = input().rstrip().split()
    u, v = to_num(u), to_num(v)
    
    graph[u].append([v])
    graph[v].append([u])
    capacity[u][v] += int(w)
    capacity[v][u] += int(w)
    

while True:
    prev = [-1 for _ in range(node_len)]
    deq = deque([0])
    while deq:
        cur = deq.popleft()
        if cur == fin:
            break;
        
        for next in graph(cur):
            if (capacity[cur][next] - flow[cur][next]) > 0 and prev[next] == -1:
                deq.append(next)
                prev[next] = cur
    
    if prev[fin] == -1:
        break
    
    min_flow = float('inf')
    find_min(fin)
    make_flow(fin)
    total_flow += min_flow