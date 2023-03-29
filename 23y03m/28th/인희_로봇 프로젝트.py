import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())

        if n <= 1:
            print('danger')
            break

        lego = []
        for _ in range(n):
            lego.append(int(input()))

        lego.sort()

        start = 0
        end = n-1

        while True:
            sums = lego[start] + lego[end]

            if sums == x:
                print('yes', lego[start], lego[end])
                break
            elif sums > x:
                end -= 1
            else:
                start += 1
            
            if start >= end:
                print('danger')
                break
    except:
        break