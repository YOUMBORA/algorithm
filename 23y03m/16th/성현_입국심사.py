def solution(n, times):
    times.sort()
    answer = 0
    left = 1
    right = times[-1]*n
    while left <= right:
        # mid는 심사에 걸린 시간(분)
        mid = (left+right) //2
        people = 0
        for t in times:
            people += mid // t 
            if people >= n:
                break
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid +1
    return answer