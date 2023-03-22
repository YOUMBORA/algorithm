import sys
import heapq

V,E = map(int,input().split())
## 1~V -> 0~V-1
start_node = int(input())-1

edges = []
## (u,v,w) = (start,end,weight)
for _ in range(E):
    edges.append(list(map(int, sys.stdin.readline().split())))

graph = [[] for _ in range(V)]

for edge in edges:
    start = edge[0]-1
    end = edge[1]-1
    graph[start].append((end, edge[2]))

def dijkstra(adj_list, start_node, n):
    INF = 1e9
    dist = [INF]*n
    dist[start_node] = 0
    
    heap_list = []
    heapq.heappush(heap_list, (0, start_node))
    
    while heap_list:
        cur_dist, cur_node = heapq.heappop(heap_list)
        
        for end_node, weight in adj_list[cur_node]:
            if (dist[end_node] > cur_dist + weight):
                dist[end_node] = cur_dist + weight
                heapq.heappush(heap_list, (dist[end_node], end_node))
    
    return dist
       
results = dijkstra(graph, start_node, V)

for result in results:
    if result == 1e9:
        print("INF")
    else:
        print(result)
