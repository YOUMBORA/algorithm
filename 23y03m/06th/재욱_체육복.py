def solution(n, lost, reserve):
    
    reserve_ = list(set(reserve) - set(lost))
    lost_ = list(set(lost) - set(reserve))

    for i in reserve_:
        if i - 1 in lost_:
            lost_.remove(i - 1)
            
        elif i + 1 in lost_:
            lost_.remove(i + 1)

    return n - len(lost_)

solution(5, [4, 2, 1], [5, 2, 4])
