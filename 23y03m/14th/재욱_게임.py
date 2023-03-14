import sys

input = sys.stdin.readline

def binary(X, Y, origin):
    answer = 0
    start = 1
    end = X
    
    
    while start <= end:
        mid = (start + end) // 2
        
        if (Y+mid)*100 // (X+mid) <= origin:
            start = mid+1
        else:
            answer = mid
            end = mid - 1
            
    print(answer)

X, Y = map(int, input().split())

origin = int(Y * 100/X)


if origin >= 99:
    print(-1)
    
else:
    binary(X, Y, origin)
