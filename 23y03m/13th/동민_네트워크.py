def dfs(n, computers):
    unvisited = [num for num in range(n)]
    stack = []
    network_cnt = 0
    while unvisited:
        stack.append(unvisited[0])
        unvisited = unvisited[1:]
        while stack:
            cur_node = stack.pop()
            for id in range(n):
                if (computers[cur_node][id] == 1) and (id in unvisited):
                    stack.append(id)
                    unvisited.remove(id)
        network_cnt += 1
    return network_cnt

def solution(n, computers):
    
    answer = dfs(n, computers)
    
    return answer
