import sys
from collections import deque
from copy import deepcopy
from itertools import combinations

def bfs(graph_copy, count):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    
    queue = deque()
    
    for i in range(n):
        for t in range(m):
            if graph_copy[i][t] == 2:
                queue.append((i,t))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph_copy[nx][ny] == 0:
                graph_copy[nx][ny] = 2
                queue.append((nx, ny))
                
    for i in range(n):
        for t in range(m):
            if graph_copy[i][t] == 0:
                cnt += 1

    return max(count, cnt)

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
count = 0
combinations_list = [x for x in range(n*m)]

for one, two, three in combinations(combinations_list, 3):
    
    if graph[one//m][one%m] == 0 and graph[two//m][two%m] == 0 and graph[three//m][three %m] == 0:
        graph_copy = deepcopy(graph)
        graph_copy[one//m][one%m] = 1
        graph_copy[two//m][two%m] = 1
        graph_copy[three//m][three%m] = 1
        
        count = bfs(graph_copy, count)        

print(count)