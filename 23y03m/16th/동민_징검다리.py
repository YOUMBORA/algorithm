def solution(distance, rocks, n):
    sorted_rocks = sorted(rocks)
    
    start = 0
    end = distance
    
    while start <= end:
        ## mid : answer가 될 것임. 근데 처음엔 찍음
        # print(start, end)
        mid = (start+end)//2
        ## 기준이 되는 돌
        standard_stone = 0
        ## 지워진 돌 개수
        remove_cnt = 0
        for rock in sorted_rocks:
            if (rock - standard_stone) < mid:
                remove_cnt += 1
                # print(rock)
            else:
                standard_stone = rock
        # print(remove_cnt)
        ## 만약 n개보다 더 많이 지워야 하는 상황이라면 mid를 줄여야겠지.
        if remove_cnt > n:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid
    
    return answer
