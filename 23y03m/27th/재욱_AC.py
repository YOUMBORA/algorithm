import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    func = list(input().strip())
    n = int(input())
    reverse = 0
    boolean = True
    
    n_array = deque(eval(input()))

    
    for RD in func:
        if RD == "R":
            reverse += 1
        else:
            try:
                if reverse % 2 == 0:
                    n_array.popleft()
                else:
                    n_array.pop()
            except:
                print("error")
                boolean = False
                break
    
    
    if boolean:
        if reverse % 2 == 0:
            print("[", end="")
            print(*n_array, sep=",", end="")
            print("]")
        else:
            n_array.reverse()
            print("[", end="")
            print(*n_array, sep=",", end="")
            print("]")