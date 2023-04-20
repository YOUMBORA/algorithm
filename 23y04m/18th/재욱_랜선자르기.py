import sys

input = sys.stdin.readline

def binary(graph, m):
    start = 1
    end = sum(graph) // m
    result = 0
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        
        for i in graph:
            cnt += i // mid
            
        if cnt >= m:
            start = mid +1
            result = mid
        else:
            end = mid -1
            
    print(result)

n,m  = map(int, input().split())

graph = sorted([int(input()) for _ in range(n)])

binary(graph, m)