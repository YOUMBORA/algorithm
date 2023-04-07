import sys
sys.setrecursionlimit(10**6)

N = int(input())

memo_end_1 = {1: 1, 2: 0}
memo_end_0 = {1: 0, 2: 1}

def pinary_end_1(n):
    if n not in memo_end_1.keys():
        memo_end_1[n] = pinary(n-1) - pinary_end_1(n-1)
    return memo_end_1[n]

def pinary(n):
    if n not in memo_end_1.keys():
        memo_end_1[n] = pinary_end_1(n) 
        memo_end_0[n] = pinary(n-1)
        
    return memo_end_1[n] + memo_end_0[n]

print(pinary(N))
