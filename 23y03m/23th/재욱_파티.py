import heapq
import sys

input = sys.stdin.readline

INF = 1e9

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

    return distance

n, m, X = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())

    graph[x].append((y, z))

distance = [INF] * (n+1)
reverse_dist = dijkstra(X, distance)

max_dist = -1

for i in range(1, n+1):
    distance = [INF] * (n+1)

    n_dist = dijkstra(i, distance)

    if n_dist[X] + reverse_dist[i] > max_dist:
        max_dist = n_dist[X] + reverse_dist[i]

print(max_dist)
