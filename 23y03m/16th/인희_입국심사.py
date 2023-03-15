def solution(n, times):
    answer = 0
    
    # 이분탐색은 정렬해주기
    times.sort()
    
    # 심사하는데 걸리는 시간(최소, 최대)
    start = 0
    end = max(times) * n
    
    # 이진 탐색 시작
    while start <= end:
        # mid = 심사하는데 주어지는 총 시간
        mid = (start + end) // 2
        people = 0
        # times를 돌면서
        for time in times:
            # 심사관 한 명이 심사할 수 있는 사람 수
            people += mid // time
            # 심사관 한 명이 n명 이상을 심사할 수 있다면, for문 빠져나오기
            if people >= n:
                break
        
        # 심사한 사람의 수가 심사 받아야할 사람의 수보다 많거나 같은 경우
        if people >= n:
            # 일단 answer에 저장하고, end를 줄여서 다시 돌려보기
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
        
    
    return answer