import heapq as hq 

N, M, K, X = map(int,input().split())
INF = int(1e9)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append((v,1))


def dijkstra(start):
    dist = [INF]*(N+1)
    q = []
    hq.heappush(q,(0,start))
    while q:
        cost, node = hq.heappop(q)
        if dist[node] < cost:
            continue 
        for nnode, ncost in graph[node]:
            newcost = cost+ncost 
            if dist[nnode] > newcost:
                dist[nnode] = newcost
                hq.heappush(q,(newcost,nnode))
    return dist

solk = dijkstra(X)
flag = 0
for i in range(1,N+1):
    if solk[i] == K:
        print(i)
        flag=1
if flag==0:
    print(-1)
