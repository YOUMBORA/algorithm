# from collections import deque 

# N, M  = map(int,input().split())
# graph = []
# bing = []
# for i in range(N):
#     temp = list(map(int,input().split()))
#     graph.append(temp)
#     for j, t in enumerate(temp):
#         if t > 0:
#             bing.append((i,j,t))

# d = [(0,1),(-1,0),(1,0),(0,-1)]
    
# def bfs(node, cgraph):
#     queue = deque()
#     queue.append(node)
#     visited = []
#     visited.append(node)
#     total = 0
#     while queue:
#         cnode = queue.popleft()
#         for i in d:
#             nnode = (cnode[0]+i[0],cnode[1]+i[1])
#             if nnode not in visited and cgraph[nnode[0]][nnode[1]] > 0:
#                 total+=cgraph[nnode[0]][nnode[1]]
#                 visited.append(nnode)
#                 queue.append(nnode)
#     return total

# y=0
# while True:
#     new_graph = [[0]*M for _ in range(N)]
#     new_bing = []
#     for bx, by, bt in bing:
#         c = 0
#         for i in d:
#             nx, ny = bx+i[0], by+i[1]
#             if graph[nx][ny] == 0:
#                 c += 1
#         nt = max(0, bt-c)
#         if nt > 0:
#             new_bing.append((bx,by,nt))
#             new_graph[bx][by] = nt    
#     y += 1
#     graph=new_graph
#     bing =new_bing 

#     if sum([sum(newg) for newg in new_graph]) != bfs(new_bing[0],new_graph):
#         print(y)
#         break
#     if sum([sum(newg) for newg in new_graph]) == 0:
#         print(1)
#         break 


import collections 
n,m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
queue = collections.deque()
day = 0
check = False

def bfs(a,b):
    queue.append((a,b))
    while queue:
        x, y = queue.popleft()
        visited[x][y] =True 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] != 0 and visited[nx][ny]==False:
                    visited[nx][ny] = True 
                    queue.append((nx,ny))
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1

while True:
    visited = [[False]*m for _ in range(n)]
    count = [[0]*m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i,j))
    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] <0:
                graph[i][j] =0
    if len(result) == 0:
        break 
    if len(result) >= 2:
        check=True 
        break 
    day +=1

if check:
    print(day)
else:
    print(0)