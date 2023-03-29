import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[]*n for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v): 
    for j in graph[v]:
        if visited[j] == 0:
            visited[j] = v
            dfs(j)

visited = [0] * (n+1)  

dfs(1)

for k in range(2, n+1):
    print(visited[k])