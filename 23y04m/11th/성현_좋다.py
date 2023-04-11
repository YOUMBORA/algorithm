N = int(input())
A = list(map(int,input().split()))
A.sort()

def binary(n):
    answer = 0
    for i in range(n):
        tmp = A[:i] + A[i+1:]
        start = 0
        end = len(tmp)-1
        while start < end:
            t = tmp[start] + tmp[end]    
            if t == A[i]:
                answer +=1
                break
            if t < A[i]:
                start += 1
            else:
                end -= 1
    return answer 

print(binary(N))