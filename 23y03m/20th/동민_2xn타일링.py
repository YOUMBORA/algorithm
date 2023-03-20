n = int(input())

memo = {}
memo[1] = 1
memo[2] = 2
k = 3

while k <= n:
    memo[k] = memo[k-1] + memo[k-2]
    k+=1

print(memo[n] % 10007)
