from collections import deque 

K = int(input())
W, H = map(int,input().split())
graph= [list(map(int,input().split())) for _ in range(H)]

visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
visited[0][0][0] = 1

hd = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
d = [(0,1),(1,0),(0,-1),(-1,0)]

def check(nx,ny,qk):
    if 0<=nx<H and 0<=ny<W and not visited[nx][ny][qk] and graph[nx][ny]==0:
        return True 
    return False 

def bfs():
    queue = deque([(0,0,0)])
    while queue:
        qx, qy, qk = queue.popleft()
        if (qx,qy) == (H-1,W-1):
            return visited[qx][qy][qk] -1 
        for dx, dy in d:
            nx = qx + dx 
            ny = qy + dy 
            if check(nx,ny,qk):
                queue.append((nx,ny,qk))
                visited[nx][ny][qk] = visited[qx][qy][qk]+1
        if qk < K:
            for hx, hy in hd:
                nhx = qx + hx 
                nhy = qy + hy 
                if check(nhx,nhy,qk+1):
                    queue.append((nhx,nhy,qk+1))
                    visited[nhx][nhy][qk+1] = visited[qx][qy][qk]+1
    return -1 

print(bfs())
        
        
    