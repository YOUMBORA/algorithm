import sys 
import heapq as hq 
input = lambda : sys.stdin.readline().strip()

def dijkstra(ds):
    dist = [INF]*(n+1)
    queue = []
    hq.heappush(queue,(0,ds))
    dist[ds] = 0
    while queue:
        qw, qn = hq.heappop(queue)
        if dist[qn] < qw:
            continue 
        for nw, nn in graph[qn]:
            cost = qw+nw 
            if dist[nn] > cost:
                dist[nn] = cost 
                hq.heappush(queue,(cost,nn))
    return dist

T = int(input())
for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((d,b))
        graph[b].append((d,a))
    d = [int(input()) for _ in range(t)]
    
    INF = 1e9 
    r = dijkstra(s)
    rh = dijkstra(h)
    rg = dijkstra(g)
    answer = []
    for pd in d:
        rhd = r[h] + rh[g] + rg[pd]
        rgd = r[g] + rg[h] + rh[pd]
        if rhd == r[pd] or rgd == r[pd]:
            answer.append(pd)
    answer.sort()
    for a in answer:
        print(a, end=' ')
    print()

