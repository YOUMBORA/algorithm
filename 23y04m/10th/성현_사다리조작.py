N, M, H = map(int, input().split())
graph = [[0]*(N) for _ in range(H)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1

ans = 4 

def check():
    for i in range(N):
        temp = i 
        for j in range(H):
            if graph[j][temp]:
                temp += 1
            elif temp >0 and graph[j][temp-1]:
                temp -= 1
        if temp != i:
            return False
    return True 

def dfs(cnt, x, y):
    global ans 
    if ans <= cnt:
        return 
    if check():
        ans = min(ans, cnt)
        return 
    if cnt ==3:
        return 
    for i in range(x, H):
        k=y if i==x else 0
        for j in range(k, N-1):
            if graph[i][j] ==0:
                graph[i][j] = 1
                dfs(cnt+1, i, j + 2)
                graph[i][j] = 0

ans = 4 
dfs(0,0,0)
print(ans if ans <= 3 else -1)
