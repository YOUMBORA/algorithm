'''
## [a, b] -> a는 0의 개수, b는 1의 개수
## 다음 단계에서는 b가 a자리로 가고, a개수가 a자리에 그대로 더해진 후 a개수를 b에 넣어준다.
## ex. [a, b] -> [b + a, a] -> [a + (b+a), (b+a)]

dp[1] = [0, 1]
dp[2] = [1, 0]
dp[3] = [1, 1]
dp[4] = [2, 1]

'''

import sys
input = sys.stdin.readline

n = int(input())
dp = [[]] * (n+1)


dp[1] = [0, 1]

for i in range(2, n+1):
    dp[i] = [dp[i-1][0] + dp[i-1][1], dp[i-1][0]]

if n == 1:
    print(sum(dp[1]))
else:
    print(sum(dp[i]))