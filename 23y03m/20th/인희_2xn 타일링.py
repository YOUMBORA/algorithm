'''
규칙
1 -> 1
2 -> 2
3 -> 3
4 -> 5
5 -> 8

f(x) = f(x-1) + f(x-2)
-> f(x-1) : 여기에 세워져 있는 타일 하나 붙기
-> f(x-2) : 여기에 누워져 있는 두 개의 타일 붙기
'''

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

if n == 1:
    dp[n] = 1
elif n == 2:
    dp[n] = 2
else:
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)
