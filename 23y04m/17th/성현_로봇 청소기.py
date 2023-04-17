import sys 
from collections import deque 
input = lambda : sys.stdin.readline().strip()

N, M  = map(int,input().split())
r, c, d = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
direct = [(-1,0),(0,1),(1,0),(0,-1)]
visited = [[False]*M for _ in range(N)]

visited[r][c] =1
answer = 1

while True:
    flag = 0
    for _ in range(4):
        d = (d+3)%4
        nr = r + direct[d][0]
        nc = c + direct[d][1]
        if 0<=nr<N and 0<=nc<M and graph[nr][nc]==0:
            if not visited[nr][nc]:
                visited[nr][nc] = True
                answer += 1
                r = nr
                c = nc 
                flag = 1
                break 
    if flag == 0:
        if graph[r-direct[d][0]][c-direct[d][1]] == 1:
            print(answer)
            break 
        else:
            r, c = r-direct[d][0], c-direct[d][1]