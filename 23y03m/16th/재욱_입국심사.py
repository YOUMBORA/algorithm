def binary(n, times):
    start = 0
    end = max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        
        result = 0
        for i in times:
            result += (mid // i)
        
        if result < n:
            start = mid+1
            
        else:
            end = mid-1
    
    return start
            

def solution(n, times):
    
    return binary(n, times)
