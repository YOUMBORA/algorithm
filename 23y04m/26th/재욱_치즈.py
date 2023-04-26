import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

def bfs(graph, graph_copy, visit):
    queue = deque([(0, 0)])
    visit[0][0] = True
    cnt = 0
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                visit[nx][ny] = True
                
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                elif graph[nx][ny] == 1:
                    graph_copy[nx][ny] = 0
                    cnt += 1
    
    return graph_copy, cnt

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

cheeze_cnt = 0

for i in range(n):
    for t in range(m):
        if graph[i][t] == 1:
            cheeze_cnt += 1

time = 0
answer = 0

while cheeze_cnt > 0:
    time += 1
    answer = cheeze_cnt
    
    visit = [[False] * m for _ in range(n)]
    graph_copy = deepcopy(graph)
    
    graph, cnt = bfs(graph, graph_copy, visit)
    
    cheeze_cnt -= cnt

    
print(time)
print(answer)