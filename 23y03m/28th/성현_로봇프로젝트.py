while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        g = [int(input()) for _ in range(n)]
        g.sort()
        start = 0
        end = n-1
        flag=True
        while start < end:
            if g[start] + g[end] == x:
                print('yes {} {}'.format(g[start], g[end]))
                flag=False
                break
            elif g[start] + g[end] > x:
                end -= 1
            else:
                start += 1
        if flag:
            print('danger')
    except:
        break 