import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, v, visit, move):
    queue = deque([(v, 1)])
    move[v] = 1
    visit[v] = True
    
    while queue:
        r, cnt = queue.popleft()
                
        for i in graph[r]:
            if not visit[i]:
                queue.append((i, cnt+1))
                visit[i] = True
                move[i] = cnt


n = int(input())
x, y = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
move = [-1] * (n+1)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
bfs(graph, x, visit, move)

print(move[y])
