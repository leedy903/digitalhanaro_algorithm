import sys
input = sys.stdin.readline

n = int(input())
sequences = [0] + list(map(int, input().rstrip().split())) + [0]

dp = [0 for _ in range(n + 2)]
answer = [0 for _ in range(n + 2)]
for i in range(n, -1, -1):
    if sequences[i] < sequences[i + 1]:
        dp[i] = sequences[i + 1]
        answer[i] = dp[i]
    else:
        if sequences[i] < dp[i + 1]:
            dp[i] = dp[i + 1]
            answer[i] = dp[i]

        else:
            dp[i] = sequences[i]
            answer[i] = -1
    
print(answer[1:-1])