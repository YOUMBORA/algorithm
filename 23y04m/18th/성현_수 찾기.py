N = int(input())
ns = list(map(int,input().split()))
M = int(input())
ms = list(map(int,input().split()))

ns.sort()
for m in ms:
    s = 0
    e = len(ns)-1
    flag = 0
    while s <= e:
        mid = (s+e)//2
        target = ns[mid]
        if target == m:
            print(1)
            flag = 1
            break 
        elif target > m:
            e = mid -1
        else:
            s = mid +1
    if flag == 0:
        print(0)
