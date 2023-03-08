import sys

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if (0 <= nx < n) and (0 <= ny < m):
            if graph[nx][ny] == "S":
                return False
            elif graph[nx][ny] == ".":
                graph[nx][ny] = "D"
            
                
    return True

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]


for i in range(n):
    for j in range(m):
        if graph[i][j] == "W":
            result = dfs(i, j)
            if result == False:
                print(0)
                exit()

print(1)
for i in graph:
    print(*i, sep="")
