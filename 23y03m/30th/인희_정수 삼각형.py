import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

# dp 테이블 생성
dp = [[0 for j in i] for i in triangle]

# dp 테이블에 두 번째 줄까지 입력해주기
dp[0][0] = triangle[0][0]

# n이 2일때부터!! 조건 주의하기
if n > 1:
    dp[1][0] = triangle[1][0] + dp[0][0]
    dp[1][1] = triangle[1][1] + dp[0][0]

    # 세 번째줄부터 규칙에 따라 dp 테이블 채워주기
    # 규칙 1) 삼각형의 가장 왼쪽과 가장 오른쪽에 있는 숫자는 바로 위의 숫자만 더할 수 있다.(j == 0 , j == i 일 때)
    # 규칙 2) 그 외의 경우는 위의 숫자 중 왼쪽과 오른쪽 중에서 큰 숫자를 선택한다.
    for i in range(2, n):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

print(max(dp[-1]))