import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().strip().split())
piles = list(map(int, input().strip().split()))
poles = list(map(int, input().strip().split()))

piles.sort()
poles.sort()

bases = set()
visited = [False for _ in range(n)]

def make_base_combination(index):
    for i in range(index + 1, n):
        if not visited[i]:
            visited[i] = True
            bases.add(abs(piles[i] - piles[index]))
            make_base_combination(i)
            visited[i] = False

make_base_combination(0)

max_area = -1

for base in bases:
    start, end = 0, m
    while start < end:
        mid = (start + end) // 2
        if base * poles[mid] <= r * 2 :
            start = mid + 1
        else:
            end = mid
    cur_area = round(base * poles[start - 1] / 2)
    
    if cur_area <= r:
        max_area = max(round(base * poles[start - 1] / 2, 2), max_area)

print(max_area)