def solution(citations):
    answer = 0
    for i in range(1, len(citations)+1, 1):
        h = sum(list(map(lambda x: (x-i)>0, citations)))
        if i<=h:
            answer=h
    return answer