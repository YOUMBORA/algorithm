def solution(triangle):
    dp = [0 for _ in range(len(triangle))]
    
    dp[0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        cal = dp[:]
        for t in range(len(triangle[i])):
            if t == 0:
                dp[t] = cal[0] + triangle[i][0]
            elif t == len(triangle[i])-1:
                dp[t] = cal[t-1] + triangle[i][t]
            else:
                dp[t] = max((cal[t-1] + triangle[i][t]) , (cal[t] + triangle[i][t]))
    
    return max(dp)
