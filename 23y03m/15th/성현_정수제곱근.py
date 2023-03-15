def binary(s,e):
    while s<=e:
        mid = (s+e)//2
        if mid**2 < n:
            s = mid +1 
        else:
            e = mid -1 
    return s 

n = int(input())

print(binary(0,n))