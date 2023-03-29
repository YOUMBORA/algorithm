from collections import deque
import sys

input = sys.stdin.readline

def bfs(graph, v, visit, root):

    queue = deque([(v, v)])
    visit[v] = True

    while queue:
        r, rot = queue.popleft()

        for i in graph[r]:
            if not visit[i]:
                visit[i] = True
                queue.append((i, i))
                root[i] = rot


n = int(input())

graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
root = [0] * (n+1)

for _ in range(n-1):
    x, y = map(int, input().split())

    graph[x].append(y)
    graph[y].append(x)

bfs(graph, 1, visit, root)

for i in range(2, n+1):
    print(root[i])
