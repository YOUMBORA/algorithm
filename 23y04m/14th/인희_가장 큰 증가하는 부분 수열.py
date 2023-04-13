import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
lst = list(map(int, input().split()))

# dp 테이블 만들기 -> 입력 받은 lst와 동일하게
dp = lst.copy()

# 현재 위치한 index보다 앞에 있는 값 중에서 현재 index보다 작은 값을 가진 index를 찾기
# 찾은 index의 dp값 중 가장 큰 값과 현재 값으로 dp 채우기
for i in range(n):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + lst[i])

print(max(dp))