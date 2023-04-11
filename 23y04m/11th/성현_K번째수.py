N = int(input())
K = int(input())

def binary():
    s = 1
    e = K
    answer = 0
    while s <= e:
        mid = (s+e)//2
        temp = 0
        for i in range(1,N+1):
            temp += min(mid//i, N)
        if temp >= K:
            answer = mid 
            e = mid-1
        else:
            s = mid +1 
    return answer

print(binary())