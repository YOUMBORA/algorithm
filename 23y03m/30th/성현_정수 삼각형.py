n = int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(i+1):
        if j==0:
            left = 0
        else:
            left = graph[i-1][j-1]
        if i==j:
            right = 0
        else:
            right = graph[i-1][j]
        graph[i][j]  = graph[i][j] + max(right,left)
print(max(graph[-1]))