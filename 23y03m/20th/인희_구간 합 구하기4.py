# sys.stdin.realine 안써주면 시간초과 납니다...

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = list(map(int, input().split()))
lst = [0]
dp = lst + dp

for k in range(1, n+1):
    dp[k] = dp[k] + dp[k-1]

for _ in range(m):
    i, j = map(int, input().split())

    print(dp[j] - dp[i-1])
