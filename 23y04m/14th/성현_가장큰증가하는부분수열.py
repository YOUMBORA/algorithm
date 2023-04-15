import sys 
input = lambda : sys.stdin.readline().strip()
N = int(input())
L = list(map(int,input().split()))

dp = L[:]
for i in range(N):
    for j in range(i):
        if L[i] > L[j]:
            dp[i] = max(dp[i], dp[j]+L[i])
print(max(dp))