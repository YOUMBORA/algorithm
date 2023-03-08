def solution(n, lost, reserve):
    
    lost = sorted(lost)
    reserve = sorted(reserve)
    # print(lost,reserve)
    cnt = 0
    
    for num in lost:
        
        if num in reserve:
            reserve.remove(num)
            cnt += 1
            
        elif (num-1) in reserve:
            reserve.remove(num-1)
            cnt+=1
        
        elif (num+1) in reserve and (num+1) not in lost:
            reserve.remove(num+1)
            cnt+=1
        # print(lost, reserve)
            
    return n + cnt - len(lost)
