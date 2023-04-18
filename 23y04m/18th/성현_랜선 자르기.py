K, N  = map(int,input().split())
lines = [int(input()) for _ in range(K)]

def binary(s, e, arr, target):
    while s <= e:
        mid = (s+e)//2
        temp = 0
        for a in arr:
            temp += a//mid
        if temp < target:
            e = mid -1
        else:
            s = mid +1
    return e

print(binary(1,max(lines),lines,N))