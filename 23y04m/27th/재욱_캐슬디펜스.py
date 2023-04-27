import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

def distance(x1,x2,y1,y2):
    return abs(x1-x2) + abs(y1-y2)

def bfs(graph, start_x, start_y, D):
    queue = deque([(start_x-1, start_y)])
    
    dx = [1, 0, 0]
    dy = [0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        
        if distance(start_x, x, start_y, y) > D:
            return [False, 0, 0]
        
        if graph[x][y] == 1:
            return [True, x, y]
        
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < start_x-1 and 0 <= ny < M:
                queue.append((nx, ny))
                
    return [False, 0, 0]
            
    
N, M, D = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
graph.append([[0]* M])

com_list = [i for i in range(M)]
result = 0

for first, second, third in combinations(com_list, 3):
    graph_copy = deepcopy(graph)
    move_arc = N
    count = 0
    
    while move_arc > 1:
        set_list = []
        
        set_list.append(bfs(graph_copy[:move_arc], move_arc, first, D))
        set_list.append(bfs(graph_copy[:move_arc], move_arc, second, D))
        set_list.append(bfs(graph_copy[:move_arc], move_arc, third, D))
        
        for boolean, x, y in set_list:
            if boolean and graph_copy[x][y] == 1:
                graph_copy[x][y] = 0
                count += 1
        
        move_arc -= 1
    
    result = max(result, count)
    
print(result)