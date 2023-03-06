import sys
# 재귀를 사용할 경우, 아래 코드를 꼭 작성해줄 것!!
# python의 기본 재귀 깊이 제한은 1000으로 매우 얕기 때문!!
sys.setrecursionlimit(10000)


T = int(input())

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # 좌표평면에서 상하좌우로 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < m) and (0 <= ny < n):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx, ny)

for _ in range(T):                
    m, n, k = map(int, input().split())

    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1


    cnt = 0
    for a in range(m):
        for b in range(n):
            if graph[a][b] > 0:
                dfs(a, b)
                cnt += 1

    print(cnt)