import heapq as hq 

N, M, X = map(int, input().split())
graph= [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
INF = 1e9

def dijkstra(start):
    distance = [INF]*(N+1)
    distance[start]=0
    q = []
    hq.heappush(q,(0,start))
    while q:
        dist, now = hq.heappop(q)
        if distance[now]<dist:
            continue
        for nnode, nweight in graph[now]:
            cost = dist+nweight
            if distance[nnode] > cost:
                distance[nnode] = cost
                hq.heappush(q,(cost,nnode))
    return distance 

answer = 0
back = dijkstra(X)
for i in range(1, N+1):
    go = dijkstra(i)
    answer = max(answer, go[X]+back[i])

print(answer)
