def solution(n, costs):
    
    visited = [costs[0][0]]
    answer = 0
    while len(visited)<n:
        new_list = []
        for cost in costs:
            if cost[0] in visited and cost[1] in visited:
                costs.remove(cost)
        for cost in costs:
            if cost[0] in visited:
                new_list.append(cost)
            elif cost[1] in visited:
                new_list.append(cost)
        # print(f"new_list={new_list}")
        shortest_edge = min(new_list,key=lambda x:x[2])
        # print(f"shortest_edge = {shortest_edge}")
        if shortest_edge[0] in visited:
            visited.append(shortest_edge[1])
        elif shortest_edge[1] in visited:
            visited.append(shortest_edge[0])
        costs.remove(shortest_edge)
        
        # print(f"visited={visited}, costs = {costs}")
        answer += shortest_edge[2]
        
    return answer
