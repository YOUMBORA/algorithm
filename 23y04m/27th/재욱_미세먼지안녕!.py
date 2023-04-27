import sys
from collections import deque

input = sys.stdin.readline

def move_clean(graph, start_x, start_y, min_x, max_x, dx, dy):
    move_count = 0
    x = start_x
    y = start_y
    
    while True:
        nx = x + dx[move_count]
        ny = y + dy[move_count]
        
        if nx == start_x and ny == start_y:
            break
        
        if min_x <= nx < max_x and 0 <= ny < C:
            if graph[x][y] == -1:
                graph[nx][ny] = 0
            else:
                graph[x][y] = graph[nx][ny]
                graph[nx][ny] = 0
                
            x = nx
            y = ny
            
        else:
            move_count += 1

def cleaning(graph, clean):
    first_dx = [-1, 0, 1, 0]
    first_dy = [0, 1, 0, -1]
    second_dx = [1, 0, -1, 0]
    second_dy = [0, 1, 0, -1]
    
    new_dirty = []
    
    for idx, clear in enumerate(clean):
        if idx == 0:
            move_clean(graph, clear[0], clear[1], 0, clear[0]+1, first_dx, first_dy)
            
        else:
            move_clean(graph, clear[0], clear[1], clear[0], R, second_dx, second_dy)
            
    
    for i in range(R):
        for t in range(C):
            if graph[i][t] > 0:
                new_dirty.append([i, t, graph[i][t]])
    
    return graph, new_dirty

def move_dirty(graph, clean, dirty):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    new_graph = [[0] * C for _ in range(R)]
    new_dirty = []
    
    for cx, cy in clean:
        new_graph[cx][cy] = -1
    
    while dirty:
        x, y, cnt = dirty.popleft()
         
        plus_dirty = cnt // 5
         
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
             
            if 0 <= nx < R and 0 <= ny < C and new_graph[nx][ny] != -1:
                new_graph[nx][ny] += plus_dirty
                cnt -= plus_dirty
                
        new_graph[x][y] += cnt
    
    for i in range(R):
        for t in range(C):
            if new_graph[i][t] > 0:
                new_dirty.append([i, t, new_graph[i][t]])
    
    return new_graph, new_dirty

def bfs(graph, clean, dirty, T):
    dirty_sum = 0
    
    for i in range(T):
        dirty = deque(dirty)

        graph, dirty = move_dirty(graph, clean, dirty)
        
        graph, dirty = cleaning(graph, clean)
    
    for i in range(R):
        for t in range(C):
            if graph[i][t] > 0:
                dirty_sum += graph[i][t]
                
    print(dirty_sum)

R, C, T = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(R)]

clean = []
dirty = []

for i in range(R):
    for t in range(C):
        if graph[i][t] == -1:
            clean.append([i, t])
        elif graph[i][t] > 0:
            dirty.append([i, t, graph[i][t]])
            
bfs(graph, clean, dirty, T)
