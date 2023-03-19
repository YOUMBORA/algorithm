from collections import deque

# bfs 함수
def bfs(v, visited, graph):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    
    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v] + 1


def solution(n, vertex):
    # graph를 새로 만들어서 연결된 노드끼리 묶어주기
    graph = [[] for _ in range(n+1)]

    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    # 얼마나 떨어져있는지 확인하기 위한 list
    visited = [0] * (n+1)
    
    # 1번 노드에서 bfs 실행
    bfs(1, visited, graph)
    
    # visited에서 가장 큰 값이 몇 개인지 return 하기
    return visited.count(max(visited))    