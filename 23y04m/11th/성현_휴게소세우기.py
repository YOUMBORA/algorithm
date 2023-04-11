N, M, L = map(int, input().split())
H = list(map(int,input().split()))
H.append(0)
H.append(L)
H.sort()

start , end = 1, L-1
result = 0
while start <= end:
    count = 0
    mid = (start+end)//2
    for i in range(1, len(H)):
        if H[i]-H[i-1] > mid:
            count += (H[i]-H[i-1]-1)//mid 
    if count > M:
        start = mid+1
    else:
        end = mid-1
        result = mid 
print(result)