import sys
sys.setrecursionlimit(10**6)

N = int(input())

memo = {1: 1, 2: 3}

def tiling(n):
    if n not in memo.keys():
        memo[n] = tiling(n-1) + 2*tiling(n-2)
    return memo[n]
    
print(tiling(N)%10007)
 
