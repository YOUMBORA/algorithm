from collections import deque

def check(rx,ry,rec):
    graph = [[-1]*102 for _ in range(102)]
    for r in rec:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x1<x<x2 and y1<y<y2:
                    graph[x][y] = 0
                elif graph[x][y] != 0:
                    graph[x][y] = 1
    if graph[rx][ry]==1:
        return True 
    else:
        return False

def solution(rectangle, cX, cY, iX, iY):
    visited = [[False]*102 for _ in range(102)]
    d = [(0,1),(1,0),(-1,0),(0,-1)]
    queue = deque()
    queue.append((cX*2,cY*2,0))
    visited[cX*2][cY*2] = True
    while queue:
        qx, qy, cnt = queue.popleft()
        if (qx,qy) == (iX*2,iY*2):
            return cnt//2
        for dx, dy in d:
            nx = qx+ dx
            ny = qy+ dy
            if check(nx,ny,rectangle) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny,cnt+1))        
            