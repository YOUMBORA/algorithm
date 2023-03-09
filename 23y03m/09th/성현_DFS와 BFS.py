import sys
from collections import deque

input = lambda : sys.stdin.readline().strip()

n,m,v = map(int,input().split())
graph = [[]]*(n+1)
visited = [False] * (n+1)

for _ in range(m):
    f, t = map(int, input().split())
    if graph[f] == []:
        graph[f] = [t]
    else:
        graph[f].append(t)
    if graph[t] == []:
        graph[t] = [f]
    else:
        graph[t].append(f)

def dfs(v):
    stack=[v]
    while len(stack) > 0:
        value = stack.pop()
        if not visited[value]:
            print(value, end=' ')
            visited[value] = True
        for j in sorted(graph[value],reverse=True):
            if not visited[j]:
                stack.append(j)

def bfs(v):
    queue = deque()
    queue.append(v)
    while len(queue) > 0:
        value = queue.popleft()
        if not visited[value]:
            print(value, end=' ')
            visited[value] = True
            for j in sorted(graph[value]):
                if not visited[j]:
                    queue.append(j)

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
