import sys 

input = lambda : sys.stdin.readline().strip()

N, C = map(int,input().split())
W = list(map(int,input().split()))
W.sort()

def binary(start, end, target):
    while start <= end:
        mid = (start+end)//2
        if W[mid] == target:
            return mid 
        if W[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return -1 

def solution():
    if binary(0, N-1, C) >= 0:
        return 1
    i = 0 
    j = N -1
    while i < j:
        sumW = W[i] + W[j]
        if sumW == C:
            return 1
        elif sumW > C:
            j -= 1
        else:
            diff = C - sumW
            if diff != W[i] and diff != W[j] and binary(0, N-1,diff) >=0:
                return 1
            i += 1
    return 0

print(solution())


