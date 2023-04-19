def move_shark():
    g = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j]:
                x, y = i, j 
                s, d, z = graph[i][j][0]
                dist = s 
                while 0 < dist:
                    nx = x + direction[d][0]
                    ny = y + direction[d][1]
                    if 0<=nx<R and 0<=ny<C:
                        x, y = nx, ny 
                        dist -= 1
                    else:
                        if d==0 or d==2:
                            d+=1
                        elif d==1 or d==3:
                            d-=1
                        continue 
                g[x][y].append([s,d,z])
    for i in range(R):
        for j in range(C):
            graph[i][j] = g[i][j]

def catch_shark():
    global answer
    for i in range(C):
        for j in range(R):
            if graph[j][i]:
                answer += graph[j][i][0][2]
                graph[j][i].remove(graph[j][i][0])
                break 
        move_shark()
        for m in range(R):
            for n in range(C):
                if 1 < len(graph[m][n]):
                    graph[m][n].sort(key=lambda x: x[2], reverse=True)
                    while 1<len(graph[m][n]):
                        graph[m][n].pop()

R, C, M = map(int,input().split())
direction = [(-1,0),(1,0),(0,1),(0,-1)]
graph = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    graph[r-1][c-1].append([s,d-1,z])

answer = 0
catch_shark()
print(answer)


# R,C,M = map(int,input().split())
# graph = [[[[0,0,0]] for _ in range(C)] for _ in range(R)]
# for _ in range(M):
#     r,c,s,d,z = map(int,input().split())
#     graph[r-1][c-1].append([z,s,d])
# direction = {1:(-1,0),2:(1,0),3:(0,1),4:(0,-1)}


# y = 0
# answer = 0
# while y < C:
#     for i in range(R):
#         if graph[i][y][0][0] >0:
#             answer += graph[i][y][0][0]
#             graph[i][y].pop(0)
#             graph[i][y].append([0,0,0])
#     for i in range(R):
#         for j in range(C):
#             if graph[i][j][0][0] >0:
#                 z,s,d = graph[i][j][0]
#                 dx,dy = direction[d]
#                 if i+s*dx >= R:
#                     nx = R-1
#                 elif i+s*dx < 0:
#                     nx = 0
#                 else:
#                     nx = i+s*dx 
#                 if i+s*dy >= C:
#                     ny = C-1
#                 elif i+s*dy < 0:
#                     ny = 0
#                 else:
#                     ny = i+s*dy 
#                 graph[nx][ny].append([z,s,d])
#                 graph[i][j].append([0,0,0])
#     for i in range(R):
#         for j in range(C):
#             if len(graph[i][j])>0:
#                 graph[i][j].sort(key=lambda x: -x[0])
#                 while len(graph[i][j])>1:
#                     graph[i][j].pop()
#     y+=1
# print(answer)