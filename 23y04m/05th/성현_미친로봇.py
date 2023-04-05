N, Ep, Wp, Sp, Np = map(int, input().split())
d = [(1,0),(-1,0),(0,1),(0,-1)]
p = [Ep, Wp, Sp, Np]
answer = 0

def dfs(x, y, visited, total):
    global answer
    if len(visited) == N+1:
        answer += total 
        return 
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if (nx, ny) not in visited:
            visited.append((nx,ny))
            dfs(nx,ny,visited,total*p[i])
            visited.pop()

dfs(0, 0, [(0,0)], 1)
print(answer*(0.01**N))