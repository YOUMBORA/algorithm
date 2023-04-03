import sys 
from collections import deque
input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())
graph = []
for i in range(N):
    temp = list(input())
    graph.append(temp)
    for j,t in enumerate(temp):
        if t == 'R':
            rx, ry = i ,j 
        elif t == 'B':
            bx, by = i, j 

d = [(-1,0), (1,0), (0,1), (0,-1)]
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

q = deque()
q.append((rx,ry,bx,by,1))
visited[rx][ry][bx][by] = True 

def move(x,y,dx,dy):
    c = 0
    while graph[x + dx][y + dy] != '#' and graph[x][y] != 'O':
        x += dx 
        y += dy 
        c += 1
    return x, y, c 

def bfs():
    while q:
        crx, cry, cbx, cby, cnt = q.popleft()
        if cnt> 10:
            break 
        for i in range(4):
            nrx, nry, rc = move(crx, cry, *d[i])
            nbx, nby, bc = move(cbx, cby, *d[i])
            if graph[nbx][nby] != 'O':
                if graph[nrx][nry] == 'O':
                    print(cnt)
                    return
                if nrx == nbx and nry == nby:
                    if rc > bc:
                        nrx -= d[i][0]
                        nry -= d[i][1]
                    else:
                        nbx -= d[i][0]
                        nby -= d[i][1]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True 
                    q.append((nrx, nry, nbx, nby, cnt+1))
    print(-1)

bfs()
