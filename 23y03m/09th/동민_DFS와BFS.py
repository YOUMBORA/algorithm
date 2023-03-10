from collections import defaultdict, deque

def dfs(nodes, adj_dict, start_node):
    visited = [False]*(nodes+1)
    stack = [start_node]
    temp_dict = defaultdict(list)
    result = []
    for key in adj_dict.keys():
        temp_dict[key] = sorted(adj_dict[key], reverse=True)[:]
    while stack:
        cur_node = stack.pop()
        if not visited[cur_node]:
            visited[cur_node] = True
            result.append(cur_node)
            for node in temp_dict[cur_node]:
                if visited[node]==False:
                    stack.append(node)
    print(*result)
        
def bfs(nodes, adj_dict, start_node):
    visited = [False]*(nodes+1)
    queue = deque()
    queue.append(start_node)
    result = []
    temp_dict = defaultdict(list)
    for key in adj_dict.keys():
        temp_dict[key] = sorted(adj_dict[key])[:]
    while queue:
        cur_node = queue.popleft()
        if not visited[cur_node]:
            visited[cur_node] = True
            result.append(cur_node)
            for node in temp_dict[cur_node]:
                if visited[node]==False:
                    queue.append(node)
    print(*result)

def solution():
    nodes, edges, start_node = list(map(int, input().split()))
    graph = []
    for i in range(edges):
        graph.append(list(map(int, input().split())))
    adj_dict = defaultdict(list)
    
    for edge in graph:
        adj_dict[edge[0]].append(edge[1])
        adj_dict[edge[1]].append(edge[0])

    dfs(nodes, adj_dict, start_node)
    bfs(nodes, adj_dict, start_node)

solution()
