import sys
from collections import deque 

input = lambda : sys.stdin.readline().strip()

n, l, m = map(int, input().split())
graph = [list(map(int,input().split()))for _ in range(n)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]
answer = 0
while True:
  visited = [[False]*(n+1) for _ in range(n+1)]
  move = False
  for r in range(n):
      for c in range(n):
          if not visited[r][c] :
            visited[r][c] = True
            queue = deque([[r,c]])
            t = [[r,c]]
            while queue:
                x,y = queue.popleft()
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                      if l<=abs(graph[nx][ny]-graph[x][y])<=m:
                        visited[nx][ny] = True
                        queue.append([nx,ny])
                        t.append([nx,ny])
            if len(t) > 1:
              move = True 
              avg = sum(graph[x][y] for x, y in t) // len(t)
              for x,y in t:
                graph[x][y] = avg
  if not move:
     break
  else:
     answer+=1
print(answer)     