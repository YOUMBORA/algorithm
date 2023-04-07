import heapq as hq 
import sys 
input = lambda : sys.stdin.readline().strip()

INF = 1e9
n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]
dist = [[INF]*n for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

x, y = 0,0
def dijkstra(bx,by):
    queue = []
    hq.heappush(queue, (bx,by,0))
    dist[bx][by] = 0
    while queue:
        qx, qy, qnt = hq.heappop(queue)
        if dist[qx][qy] < qnt:
            continue
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 0:
                    nnt = qnt + 1
                else:
                    nnt = qnt 
                if dist[nx][ny]>nnt :
                    dist[nx][ny] = nnt
                    hq.heappush(queue,(nx,ny,nnt))
    
dijkstra(0,0)
print(dist[n-1][n-1])