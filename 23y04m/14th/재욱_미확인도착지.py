import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def dijkstra(start):
    dp = [inf for _ in range(n + 1)]
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])

    while heap:
        x, y = heappop(heap)
        for xx, yy in graph[y]:
            xy = x + yy
            if dp[xx] > xy:
                dp[xx] = xy
                heappush(heap, [xy, xx])
    return dp

inf = 1e9
T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())
    start, g, h = map(int, input().split())
    
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        x, y, dist = map(int, input().split())
        graph[x].append([y, dist])
        graph[y].append([x, dist])
        
    candidate = sorted([int(input()) for _ in range(t)])
    
    start_dijkstra = dijkstra(start)
    candidate_g_dijkstra = dijkstra(g)
    candidate_h_dijkstra = dijkstra(h)
    
    for i in candidate:
        if start_dijkstra[g] + candidate_g_dijkstra[h] + candidate_h_dijkstra[i] == start_dijkstra[i] or start_dijkstra[h] + candidate_h_dijkstra[g] + candidate_g_dijkstra[i] == start_dijkstra[i]:
            print(i, end=" ")
    
    print()
    
    
        