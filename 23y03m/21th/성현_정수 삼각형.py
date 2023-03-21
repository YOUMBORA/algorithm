def solution(tr):
    dp = [[0] * len(tr) for _ in range(len(tr))]
    for i, t in enumerate(tr):
        dp[i][0] = dp[i-1][0] + t[0]
        for j, u in enumerate(t):            
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + u
    return max(dp[-1])