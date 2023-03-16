def solution(distance, rocks, n):
    rocks.sort()
    start = 0
    end = distance
    while(start <= end):
        mid = (start+end)//2
        p_stone = 0
        no = 0
        for r in rocks:
            if r - p_stone < mid:
                no +=1
            else:
                p_stone = r
        if no > n:
            end = mid-1
        else:
            answer = mid
            start = mid+1
    return answer