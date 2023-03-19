def solution(triangle):
    # dp 테이블 초기화 -> triangle과 똑같은 list 형태로 만들어주기
    dp = [[0 for j in i] for i in triangle]
    # dp 첫 번째 칸은 삼각형 꼭대기 하나의 값 넣어주기
    dp[0][0] = triangle[0][0]
    
    # 삼각형의 두 번째 줄부터 차례로 돌면서
    for i in range(1, len(triangle)):
        for j in range(i):
            # ex) 셋째 줄은 8, 1에 각각 3 자리에 해당하는 더한 값을 더해주게 된다.
            #       그 후, 1은 앞에서 3 자리에 해당하는 값을 더해준 결과와 8자리에 해당하는 값을 더해준 결과 중 더 큰 것을 고르고 넣어준다.
            dp[i][j] = max(dp[i][j], dp[i-1][j] + triangle[i][j])
            dp[i][j+1] = dp[i-1][j] + triangle[i][j+1]
    
    # 마지막 삼각형 줄에서 가장 큰 값을 가져온다.
    return max(dp[-1])