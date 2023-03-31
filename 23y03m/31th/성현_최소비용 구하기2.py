import heapq as hq 

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
s, e = map(int,input().split())

def dijkstra(start):
    distance = [INF]*(n+1)
    prev = [0] *(n+1)
    queue = []
    hq.heappush(queue,(0,start))
    distance[start]=0
    while queue:
        cost, node = hq.heappop(queue)
        if distance[node] < cost:
            continue
        for nnode, ncost in graph[node]:
            new_cost = cost+ncost
            if distance[nnode] > new_cost:
                distance[nnode] = new_cost
                prev[nnode] = node
                hq.heappush(queue,(new_cost,nnode))
    return distance, prev

dist, path = dijkstra(s)
print(dist[e])

p = [e]
now = e 
while now != s:
    now = path[now]
    p.append(now)
p.reverse()

print(len(p))
print(' '.join(map(str,p)))
