def binary(nx, lx, kx):
    answer =0
    value = 1e9
    for i in range(nx):
        start = i+1
        end = nx-1
        while start <= end:
            mid = (start+end)//2
            avg = lx[i] + lx[mid]
            if avg > kx:
                end = mid-1
            else:
                start = mid+1
            if abs(avg-kx) < value:
                answer = 1
                value = abs(avg-kx)
            elif abs(avg-kx) == value:
                answer +=1
    return answer         

t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    n_list = list(map(int,input().split()))
    n_list.sort()
    print(binary(n,n_list,k))