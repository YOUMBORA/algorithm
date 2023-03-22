import sys
import heapq
input = sys.stdin.readline
INF = 1e9

# 입력 받기
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
start_city, end_city = map(int, input().split())

distance = [INF] * (n+1)

def dijkstra(start):
    distance[start] = 0
    queue = [(0, start)]

    while queue:
        cost, now = heapq.heappop(queue)
        if distance[now] < cost:
            continue

        for a, b in graph[now]:
            now_cost = distance[now] + b
            if distance[a] > now_cost:
                distance[a] = now_cost
                heapq.heappush(queue, (now_cost, a))

dijkstra(start_city)
print(distance[end_city])


