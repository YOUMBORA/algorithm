import sys 
from collections import deque
input = lambda : sys.stdin.readline().strip()

n, m = map(int,input().split())
graph = [[]]*(n+1)

for _ in range(m):
    r1, r2 = map(int, input().split())
    if graph[r2] == []:
        graph[r2] = [r1]
    else:
        graph[r2].append(r1)

def dfs(v):
    visited = [False] * (n+1)
    stack = [v]
    c = 0
    while len(stack) > 0:
        value = stack.pop()
        if not visited[value]:
            visited[value] = True 
            c += 1
        for i in graph[value]:
            if not visited[i]:
                stack.append(i)
    return c 

def bfs(v):
    visited = [False] * (n+1)
    queue = deque()
    queue.append(v)
    c= 0 
    while len(queue) >0:
        value = queue.popleft()
        if not visited[value]:
            visited[value] = True 
            c+=1 
            for i in graph[value]:
                if not visited[i]:
                    queue.append(i)
    return c

result = []
for j in range(n+1):
    result.append(bfs(j))

for i, r in enumerate(result):
    if r == max(result):
        print(i, end = ' ')