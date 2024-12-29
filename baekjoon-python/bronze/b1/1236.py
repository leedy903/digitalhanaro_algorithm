import sys
input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(n)]

def get_count(matrix):
    count = 0
    for i in range(len(matrix)):
        if 'X' not in matrix[i]:
            count += 1
    return count

ans = max(get_count(matrix), get_count(list(map(list, zip(*matrix)))))

print(ans)