import sys
import heapq
input = sys.stdin.readline

# 입력 받기
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

INF = 1e9
distance = [INF] * (n+1)

# 다익스트라
def dijkstra(start, distance):
    distance[start] = 0
    queue = [(0, start)]

    while queue:
        cost, now = heapq.heappop(queue)

        if distance[now] < cost:
            continue

        for a, b in graph[now]:
            now_cost = cost + b

            if distance[a] > now_cost:
                distance[a] = now_cost
                heapq.heappush(queue, (now_cost, a))
        print(distance)
    return distance

times = 0
for j in range(1, n+1):
    go = dijkstra(j, distance)
    back = dijkstra(x, distance)
    times = max(times, go[j] + back[x])
    print(times)

print(times)