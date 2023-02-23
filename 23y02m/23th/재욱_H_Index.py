def solution(citations):
    citations.sort(reverse = True)  
    cnt = 0

    for idx, i in enumerate(citations):
        if i >= idx+1:
            cnt += 1
    return cnt
