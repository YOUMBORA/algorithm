import sys
    
def binary(n, max_):
    
    start = 0
    end = max(n)
    find = 0
    result = 0
    
    while start <= end:
        mid = (start+end) // 2
        
        for i in n:
            if i > mid:
                find += mid
            else:
                find += i
        
        if find <= max_:
            result = mid
            start = mid + 1
            find = 0
        else:
            end = mid - 1
            find =0
            
    print(result)
            
T = int(input())

n = sorted(map(int, input().split()))

max_ = int(input())

binary(n, max_)

### 오답 예시

# import sys
# from bisect import bisect_left, bisect_right

# input = sys.stdin.readline

# def bi(n, divid, max_):
#     x = bisect_right(n, divid)
    
#     sum_n = sum(n[:x])
#     max_ -= sum_n
    
#     length = len(n) - x
    
#     if length == 1:
#         print(n[-1])
#     else:
#         print(max_ // length)
    

# T = int(input())

# n = sorted(map(int, input().split()))

# max_ = int(input())
# divid = max_ // T

# if sum(n) <= max_:
#     print(max(n))

# else:
#     bi(n, divid, max_)
