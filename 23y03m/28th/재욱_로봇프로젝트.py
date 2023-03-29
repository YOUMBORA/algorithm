import sys

input = sys.stdin.readline

def binary(x, n, lego):

    start = 0
    end = n-1

    while start < end:
        if lego[start] + lego[end] == x:
            return lego[start], lego[end], True
        
        elif lego[start] + lego[end] < x:
            start += 1
        else:
            end -= 1


    return 0, 0, False

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        lego = sorted([int(input()) for _ in range(n)])


        l1, l2, boolean = binary(x, n, lego)

        if boolean:
            print(f"yes {l1} {l2}")
        else:
            print('danger')
    
    except:
        break
