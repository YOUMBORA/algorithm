import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * n

candidate = list(map(int, input().split()))

dp[0] = candidate[0]


for i in range(1, n):
    dp[i] = max(dp[i-1] + candidate[i], candidate[i])
    
print(max(dp))
