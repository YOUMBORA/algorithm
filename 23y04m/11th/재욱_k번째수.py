import sys

input = sys.stdin.readline

N = int(input())
k = int(input())

s = 1
e = N * N

while s <= e :
    m = (s+e) // 2
    cnt = 0
    
    for i in range(1, N+1):
#         print(m//i, N)
        cnt += min(m//i, N)
    
    if cnt >= k :
        e = m-1
    else:
        s = m+1
        
print(s)
