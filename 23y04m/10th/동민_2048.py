import sys
from copy import deepcopy

def permutation_with_replacement(array, n):
    for i in range(len(array)):
        if n == 1:
            yield [array[i]]
        else:
            for next in permutation_with_replacement(array, n-1):
                yield [array[i]] + next

def move_east(graph, n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                graph[i].pop(j)
                graph[i].insert(0,0)

    for row in graph:
        for num in range(len(row)-1,-1,-1):
            if num == 0:
                break
            if row[num] == row[num - 1]:
                row[num-1] += row.pop(num)
                row.insert(0,0)

    return graph

def move_west(graph, n):
    for i in range(n):
        for j in range(n-1,-1,-1):
            if graph[i][j] == 0:
                graph[i].pop(j)
                graph[i].append(0)

    for row in graph:
        for num in range(len(row)):
            if num == len(row)-1:
                break
            if row[num] == row[num + 1]:
                temp = row.pop(num)
                row[num] += temp
                row.append(0)

    return graph

def rotate_clock_90(graph,n):
    new_graph = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_graph[j][n-1-i] = graph[i][j]
    return new_graph

def rotate_counter_90(graph,n):
    new_graph = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_graph[n-1-j][i] = graph[i][j]
    return new_graph

def main():
    N = int(input())

    origin_graph = []
    for _ in range(N):
        origin_graph.append(list(map(int, sys.stdin.readline().split())))
    
    result = 0
    for perm in permutation_with_replacement([0,1,2,3], 5):
        graph = deepcopy(origin_graph)

        for dir in perm:
            if dir == 0:
                graph = move_east(graph, N)
            elif dir == 1:
                graph = rotate_clock_90(graph, N)
                graph = move_west(graph, N)
                graph = rotate_counter_90(graph, N)
            elif dir == 2:
                graph = move_west(graph, N)
            elif dir == 3:
                graph = rotate_clock_90(graph, N)
                graph = move_east(graph, N)
                graph = rotate_counter_90(graph, N)

        temp_result = max([max(x) for x in graph])
        result = max(temp_result, result)
    
    print(result)

main()
