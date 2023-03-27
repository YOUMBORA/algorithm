import heapq as hq 

N, E = map(int, input().split())
graph = [[] for i in range(N+1)]
INF = 1e9

for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))


def dijkstra(start):
    dp = [INF for i in range(N+1)]
    dp[start]=0
    heap = []
    hq.heappush(heap,[0,start])
    while heap:
        w, c = hq.heappop(heap)
        for nn, nw in graph[c]:
            cost = nw + w
            if dp[nn] > cost:
                dp[nn] = cost 
                hq.heappush(heap,[cost,nn])
    return dp

v1, v2 = map(int, input().split())

one = dijkstra(1)
r1 = dijkstra(v1)
r2 = dijkstra(v2)

answer = min(one[v1]+r1[v2]+r2[N], one[v2]+r2[v1]+r1[N])
print(answer if answer < INF else -1)