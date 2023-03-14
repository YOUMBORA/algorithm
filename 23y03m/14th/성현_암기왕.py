def binary_search(s, e, x, y):
    while s <= e:
        mid = (s+e)//2
        if x[mid] == y:
            return 1
        elif x[mid] < y:
            s = mid+1
        else:
            e = mid-1
    return 0

T = int(input())
for _ in range(T):
    N = int(input())
    n1 = [i for i in map(int,input().split())]
    M = int(input())
    n2 = [i for i in map(int,input().split())]
    n1.sort()
    for k in n2:
        print(binary_search(0,N-1, n1, k))