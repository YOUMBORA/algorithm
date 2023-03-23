import heapq as hq 

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
INF = 1e6
distance = [INF]*(N+1)

def dijkstra(start):
    q = []
    hq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        nd, nnode = hq.heappop(q)
        if distance[nnode] < nd:
            continue
        for cnode, cd in graph[nnode]:
            ncost = nd + cd
            if distance[cnode] > ncost:
                distance[cnode] = ncost
                hq.heappush(q,(ncost,cnode))
    return distance
s, e = map(int, input().split())

print(dijkstra(s)[e])

