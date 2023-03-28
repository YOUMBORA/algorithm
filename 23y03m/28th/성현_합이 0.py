from collections import Counter 

N = int(input())
A = list(map(int,input().split()))
A.sort()
scount = Counter(A)
result = 0

for i, a in enumerate(A):
    left, right = i+1, N-1
    while left < right:
        s = A[left] + A[right] + A[i]
        if s == 0:
            if A[left] == A[right]:
                result += right - left
            else:
                result += scount[A[right]]
            left += 1
        elif s > 0:
            right -= 1
        elif s <0:
            left += 1

print(result)