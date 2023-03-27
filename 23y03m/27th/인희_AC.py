from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    lst = deque(input().replace('[','').replace(']','').split(','))

    R = 0
    left = 0
    right = 0
    for case in p:
        if case == 'D':
            if R % 2 == 0:
                left += 1
            else:
                right += 1
        else:
            R += 1

    if right + left <= n:
        while right != 0:
            lst.pop()
            right -= 1
        
        while left != 0:
            lst.popleft()
            left -= 1

        if R % 2 != 0:
            lst.reverse()   

        print('['+','.join(lst)+']')
    else:
        print("error")
    

