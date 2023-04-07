'''
내가 DP 푸는 방법 -> list를 돌면서 기준이 되는 값을 비교하며 현재 값을 갱신해 나가는 것(or 누적합)

(현재 index의 값, 이전 index(누적 합)와 현재 index의 값) 의 크기를 비교하자. 
전자가 더 크다면, 이전의 누적 값은 버리고(연속하지 않으므로) 현재 값부터 새로 누적해 나가자.
후자가 더 크다면, 계속해서 누적합을 쌓아나가자.
'''

import sys
input = sys.stdin.readline

n = int(input())
dp = list(map(int, input().split()))

for i in range(1, n):
    dp[i] = max(dp[i], dp[i-1] + dp[i])

print(max(dp))