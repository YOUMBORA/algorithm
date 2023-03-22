import sys 
import heapq 

input = sys.stdin.readline 
INF = sys.maxsize 
V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
dist = [INF]*(V+1)
heap = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w,v))

def dijkstra(start):
    dist[start]= 0
    heapq.heappush(heap, (0, start))

    while heap:
        w1, now = heapq.heappop(heap)
        if dist[now] < w1:
            continue
        for w2, next_node in graph[now]:
            if w1+w2 < dist[next_node]:
                dist[next_node] = w1+w2
                heapq.heappush(heap,(w1+w2,next_node))

dijkstra(K)
for i in range(1,V+1):
    print("INF" if dist[i] == INF else dist[i])
