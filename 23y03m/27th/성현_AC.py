from collections import deque 

T = int(input())
for _ in range(T):
    p =input()
    n = int(input())
    a = input()[1:-1].split(',')
    
    qa = deque(a)

    flag = 0

    if n == 0:
        qa = []

    for q in p:
        if q == 'R':
            flag += 1
        elif q == 'D':
            if len(qa) == 0:
                print('error')
                break
            else:
                if flag % 2 == 0:
                    qa.popleft()
                else:
                    qa.pop()
    else:
        if flag %2 ==0:
            print("[" + ",".join(qa) + "]")
        else:
            qa.reverse()
            print("[" + ",".join(qa) + "]")