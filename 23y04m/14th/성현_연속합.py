import sys 
input = lambda : sys.stdin.readline().strip()
N = int(input())
L = list(map(int,input().split()))

for i in range(1,len(L)):
    L[i] = max(L[i-1]+L[i],L[i])
print(max(L))