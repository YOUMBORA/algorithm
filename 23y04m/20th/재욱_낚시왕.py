import sys
from collections import deque

input = sys.stdin.readline

def shark_move(s_x, s_y, s_speed, s_direct, s_size):
    dx = [0, -1, 1, 0, 0] # 북 남 동 서 
    dy = [0, 0, 0, 1, -1]
    direct_change = {1 : 2, 2 : 1, 3: 4, 4: 3}
    count = s_speed
    
    while count > 0:
        s_x += dx[s_direct]
        s_y += dy[s_direct]
        
        if 0 <= s_x < N and 0 <= s_y < M:
            count -= 1
        else:
            s_x -= dx[s_direct]
            s_y -= dy[s_direct]
            s_direct = direct_change[s_direct]
            
            s_x += dx[s_direct]
            s_y += dy[s_direct]
            
            count -= 1
    return [s_x, s_y, s_speed, s_direct, s_size]

def shark_check(graph):
    check_list = []
    
    for i in range(M):
        for t in range(N):
            if graph[t][i] != 0:
                s, d, z = graph[t][i]
                check_list.append(shark_move(t, i, s, d, z))
                graph[t][i] = 0
    
    for x, y, s, p, z in check_list:
        if graph[x][y] == 0:
            graph[x][y] = [s, p, z]
        else:
            if graph[x][y][-1] < z:
                graph[x][y] = [s, p, z]
    
    return graph

def catch(graph):
    cnt = 0
        
    for i in range(M):
        for t in range(N):
            if graph[t][i] != 0:
                cnt += graph[t][i][-1]
                graph[t][i] = 0
                break
            
        shark_check(graph)
    
    print(cnt)
    

N, M, K = map(int, input().split())

graph = [[0] * (M) for _ in range(N)]

for _ in range(K):
    x, y, s, d, z = map(int, input().split())
    
    graph[x-1][y-1] = [s, d, z]
    
catch(graph)