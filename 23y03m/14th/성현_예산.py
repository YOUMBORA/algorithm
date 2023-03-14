def binary_search(s,e,y,l):
    while s <= e:
        mid = (s+e)//2
        total = 0
        for yy in y:
            if yy > mid:
                total += mid
            else:
                total += yy
        if total <= l:
            s = mid + 1
        else:
            e = mid - 1 
        print(total)
        print(e)
    return e 

N = int(input())
Y = [i for i in map(int,input().split())]
L = int(input())

print(binary_search(0, max(Y),Y,L))