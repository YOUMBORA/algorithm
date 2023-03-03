# for문을 사용해서 wires에서 하나씩 끊어보기
# dfs를 이용하여 각각의 송전탑 개수를 구한 후, 차이를 list에 넣어주기
# list의 최소값 구하기

# dfs를 잘 못해서 생기는 대참사 발생

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            

def solution(n, wires):
    answer = -1
    
    for idx in range(len(wires)):
        wire = wires.copy()
        del wire[idx]

        visited = [False] * (n+1)
        dfs(wire, 1, visited)
    
    return answer