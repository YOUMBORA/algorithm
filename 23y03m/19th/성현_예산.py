def binary(left, right, x, y):
    while left<=right:
        mid = (left+right)//2
        total = 0
        for a in x:
            if a > mid:
                total += mid
            else:
                total += a 
        if total <= y:
            left = mid +1
        else:
            right = mid -1
    return right 

n = int(input())
t = list(map(int,input().split()))
m = int(input())

print(binary(0, max(t), t, m))
