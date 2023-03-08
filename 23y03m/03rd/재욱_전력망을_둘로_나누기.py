def DFS(v, graph, visited, check):
    cnt = 1
    visited[v] = True
    
    for adj_v in graph[v]:
        if visited[adj_v] == False and check[v][adj_v]:
            cnt += DFS(adj_v, graph, visited, check)
    
    return cnt

def solution(n, wires):
    answer = 10000
    
    check = [[True]*(n+1) for _ in range(n+1)]
    
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    print(graph)
    
    for a, b in wires:
        visited = [False]*(n+1)
        
        check[a][b] = False
        tree1 = DFS(a, graph, visited, check)
        tree2 = DFS(b, graph, visited, check)
        check[a][b] = True
        
        answer = min(answer, abs(tree1 - tree2))
    
    return answer
