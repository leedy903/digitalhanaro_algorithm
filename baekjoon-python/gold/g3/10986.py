import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sequences = list(map(int, input().split()))
remainder = [0 for _ in range(m)]
prefix_sum = 0

for i in range(n):
    prefix_sum += sequences[i]
    remainder[prefix_sum % m] += 1
    
ans = remainder[0]
    
for remain in remainder:
    ans += remain * (remain - 1) // 2

print(ans)

