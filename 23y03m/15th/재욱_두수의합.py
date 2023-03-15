import sys

input = sys.stdin.readline

def binary(n, m, n_list):
    min_ = 1e9
    cnt =0
    
    for i in range(n):
        start = i+1
        end = n-1
        
        while start <= end:
            mid = (start + end)//2
            
            hap = n_list[i] + n_list[mid]
            if hap > m:
                end = mid -1
            else:
                start = mid + 1
            
            if abs(hap-m) < min_:
                cnt = 1
                min_ = abs(m-hap)
            elif abs(hap-m) == min_:
                cnt += 1
    
    print(cnt)

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    
    n_list = sorted(list(map(int, input().split())))
    
    binary(n, m, n_list)

