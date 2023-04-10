import sys
from itertools import product
from copy import deepcopy

input = sys.stdin.readline

def move(graph_copy, direct):
    if direct == "UP":
        for column in range(n):
            row_direction = 0
            for row in range(1, n):
                if graph_copy[row][column] == 0:
                    continue
                
                if graph_copy[row_direction][column] == graph_copy[row][column]:
                    graph_copy[row_direction][column] += graph_copy[row][column]
                    graph_copy[row][column] = 0
                else:
                    row_direction = row
        
            for i in range(n):
                if graph_copy[i][column] == 0:
                    for t in range(i, n):
                        if graph_copy[t][column] != 0:
                            graph_copy[i][column] = graph_copy[t][column]
                            graph_copy[t][column] = 0
        
    elif direct == "DOWN":
        for column in range(n):
            row_direction = n-1
            for row in range(n-2, -1, -1):
                if graph_copy[row][column] == 0:
                    continue
                    
                if graph_copy[row_direction][column] == graph_copy[row][column]:
                    graph_copy[row_direction][column] += graph_copy[row][column]
                    graph_copy[row][column] = 0
                else:
                    row_direction = row
                    
            for i in range(n-1, -1, -1):
                if graph_copy[i][column] == 0:
                    for t in range(i, -1, -1):
                        if graph_copy[t][column] != 0:
                            graph_copy[i][column] = graph_copy[t][column]
                            graph_copy[t][column] = 0
        
    elif direct == "LEFT":
        for row in range(n):
            column_direction = 0
            for column in range(1, n):
                    if graph_copy[row][column] == 0:
                        continue
                    
                    if graph_copy[row][column_direction] == graph_copy[row][column]:
                        graph_copy[row][column_direction] += graph_copy[row][column]
                        graph_copy[row][column] = 0
                    else:
                        column_direction = column

            for i in range(n):
                if graph_copy[row][i] == 0:
                    for t in range(i, n):
                        if graph_copy[row][t] != 0:
                            graph_copy[row][i] = graph_copy[row][t]
                            graph_copy[row][t] = 0
        
    elif direct == "RIGHT":
        for row in range(n):
            column_direction = n-1
            for column in range(n-2, -1, -1):
                if graph_copy[row][column] == 0:
                        continue
                    
                if graph_copy[row][column_direction] == graph_copy[row][column]:
                    graph_copy[row][column_direction] += graph_copy[row][column]
                    graph_copy[row][column] = 0
                else:
                    column_direction = column
        
            for i in range(n-1, -1, -1):
                if graph_copy[row][i] == 0:
                    for t in range(i, -1, -1):
                        if graph_copy[row][t] != 0:
                            graph_copy[row][i] = graph_copy[row][t]
                            graph_copy[row][t] = 0
    
    return graph_copy

direction = ["UP", "DOWN", "LEFT", "RIGHT"]

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

result = -1

for i in product(direction, repeat=4):
    graph_copy = deepcopy(graph)
    for t in i:
        graph_copy = move(graph_copy, t)

    result = max(result, max(map(max, graph_copy)))
    
print(result)
