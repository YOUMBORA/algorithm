from collections import deque

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

visited = [[-1] * (m) for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ( 0 <= nx < n ) and ( 0 <= ny < m ):
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y]
                        queue.appendleft([nx, ny])
                    else:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append([nx, ny])

bfs(0, 0)
print(visited[n-1][m-1])