def solution(m,n,puddles):
    grid = [[0]*(m+1) for i in range(n+1)]
    if puddles != [[]]:
        for a,b in puddles:
            grid[b][a] = -1
    grid[1][1] =1
    for j in range(1, n+1):
        for k in range(1, m+1):
            if j==k==1:
                continue
            if grid[j][k] == -1:
                grid[j][k] = 0
                continue
            grid[j][k] = (grid[j][k-1] + grid[j-1][k])
    return grid[n][m]%1000000007 