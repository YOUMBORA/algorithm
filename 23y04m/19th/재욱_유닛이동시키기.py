import sys
from collections import deque

input = sys.stdin.readline

def check(x, y, A, B):
    for i in range(A):
        for t in range(B):
            nx = x + i
            ny = y + t
            
            try:
                if graph[nx][ny] == 1:
                    return False
            except:
                return False
    
    return True

def bfs(graph, A, B, start, end, visit):
    queue = deque([(start[0]-1,start[1]-1, 0)])
    visit[start[0]-1][start[1]-1] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if x == end[0]-1 and y == end[1]-1:
            print(cnt)
            exit()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and check(nx, ny, A, B) and not visit[nx][ny]:
                queue.append((nx, ny, cnt+1))
                visit[nx][ny] = True
    
    print(-1)
                

N, M, A, B, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
visit = [[False] * M for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
      
s = list(map(int, input().split()))
e = list(map(int, input().split()))
    
bfs(graph, A, B, s, e, visit)