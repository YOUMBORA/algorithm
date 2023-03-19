# 인접한 집은 털 수 없으므로, 현재 지점에서는 (바로 전 집까지 훔칠 수 있는 최댓값)과 (전전집까지의 훔칠 수 있는 최댓값 + 현재 집의 money) 경우의 수 존재
# dp1 = 첫 번째 집을 무조건 털 때(마지막 집은 무조건 안턴다)
# dp2 = 첫 번째 집을 무조건 안 털 때(마지막 집은 털어도 되고, 안털어도 되고)

def solution(money):
    # dp 테이블 초기화
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    
    dp1[0] = money[0]
    for i in range(1, len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
        
    dp2[0] = 0
    for j in range(1, len(money)):
        dp2[j] = max(dp2[j-1], dp2[j-2] + money[j])
        
    return max(dp1[-2], dp2[-1])