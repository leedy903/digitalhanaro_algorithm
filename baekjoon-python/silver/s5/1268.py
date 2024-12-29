import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
table = [list(map(int, input().strip().split())) for _ in range(n)]
table = list(map(list, zip(*table)))

friends = defaultdict(set)

for i in range(5):
    class_map = defaultdict(list)
    for j in range(n):
        class_map[table[i][j]].append(j)
    
    for _, classmates in class_map.items():
        for classmate in classmates:
            friends[classmate].update(classmates)

ans = 0
max_count = 0
for i in range(n):
    if max_count < len(friends[i]):
        max_count = len(friends[i])
        ans = i + 1
        
print(ans)