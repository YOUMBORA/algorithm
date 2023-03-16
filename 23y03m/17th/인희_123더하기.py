'''
규칙
1 -> 1
2 -> 2
3 -> 4
4 -> 7
5 -> 13
6 -> 24
f(x) = f(x-1) + f(x-2) + f(x-3)
'''
    
# 입력 받기
T = int(input())
for j in range(T):
    n = int(input())
    
    # DP 테이블 초기화
    dp = [0] * (n+1)

    if n == 1:
        dp[1] = 1
    elif n == 2:
        dp[2] = 2
    elif n == 3:
        dp[3] = 4
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
    
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])