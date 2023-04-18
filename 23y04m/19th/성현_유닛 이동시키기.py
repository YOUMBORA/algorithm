from collections import deque

N,M,A,B,K = map(int,input().split())
obstacles = [tuple(map(lambda x: int(x)-1,input().split())) for _ in range(K)]
start = tuple(map(lambda x: int(x)-1,input().split()))
end = tuple(map(lambda x: int(x)-1,input().split()))

graph = [[0]*M for _ in range(N)]
for o in obstacles:
    graph[o[0]][o[1]] = -1

def cango(w):
    for a in range(A):
        for b in range(B):
            wx, wy = w[0]+a, w[1]+b
            if wx<0 or wx>=N or wy<0 or wy>=M or graph[wx][wy] == -1:
                return False
    return True

d = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs():
    queue = deque([(start[0],start[1],0)])
    graph[start[0]][start[1]] = 1
    while queue:
        qx,qy,qnt = queue.popleft()
        if (qx,qy) == end:
            return qnt
        for dx, dy in d:
            nx = qx+dx 
            ny = qy+dy 
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
                if cango((nx,ny)):
                    graph[nx][ny] =1
                    queue.append((nx,ny,qnt+1))
    return -1

print(bfs())