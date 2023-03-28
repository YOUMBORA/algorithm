import sys 
input = lambda : sys.stdin.readline().strip()

M, N, L = map(int,input().split())
shoot = list(map(int,input().split()))
animals = []
for _ in range(N):
    tmpx,tmpy = map(int,input().split())
    animals.append((tmpx,tmpy))

answer = 0
shoot.sort()
for x,y in animals:
    if (y>L):
        continue
    s = x+y-L
    e = x-y+L
    left, right = 0, M-1
    while left <= right:
        mid = (left+right)//2
        if shoot[mid] >= s and shoot[mid] <= e:
            answer+=1
            break 
        elif shoot[mid] < e:
            left = mid +1
        else:
            right = mid -1 
print(answer)
