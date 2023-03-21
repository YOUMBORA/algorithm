def solution(money):
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    
    dp1[0] = money[0]
    dp1[1] = 0
    
    dp2[0] = 0
    dp2[1] = money[1]
    
    for i in range(2, len(money)):
        dp1[i] = money[i] + max(dp1[i - 2], dp1[i - 3])
        dp2[i] = money[i] + max(dp2[i - 2], dp2[i - 3])
    
    dp1 = dp1[:-1]

    return max(max(dp1), max(dp2))
