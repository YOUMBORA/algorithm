## 	런타임 에러 (ZeroDivisionError)

import sys

input= sys.stdin.readline

def binary(graph, M):
    
    s = 0
    e = graph[-1]
    
    result = 0
    
    while s <= e:
        m = (s + e) // 2
        cnt = 0
        
        for i in range(1, len(graph)):
            x = graph[i] - graph[i-1]
            
            if x > m:
                cnt += (x-1) // m
        
        if cnt > M:
            s = m + 1
        else:
            e = m - 1
            result = m
    
    print(result)
    
N, M, L = map(int, input().split())

graph = [0] + sorted(list(map(int, input().split()))) + [L-1]

binary(graph, M)
