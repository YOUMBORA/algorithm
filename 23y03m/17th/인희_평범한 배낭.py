# 냅색(Knapsack) 알고리즘

n, k = map(int, input().split())  # n: 물품의 수, k: 가방에 넣을 수 있는 최대 무게

# DP 테이블 초기화
dp = [[0] * (k+1) for _ in range(n+1)]
m = [[0, 0]]

for i in range(n):
    w, v = map(int, input().split())  # w: 각 물건의 무게, v: 물건의 가치
    m.append([w, v])

print(m)
print(dp)

for i in range(1, n+1):
    w = m[i][0]
    v = m[i][1]

    for j in range(1, k+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
            print('--', dp)
        else:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
            print('==', dp)

print(dp[n][k])