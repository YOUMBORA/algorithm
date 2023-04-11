import sys

input = sys.stdin.readline

def binary(graph, n):
    good = 0
    
    for i in range(n):
        find_list = graph[:i] + graph[i+1:]
        start, end = 0, n-2
        
        while start < end:
            mid = find_list[start] + find_list[end]
            
            if mid == graph[i]:
                good += 1
                break
            
            if mid < graph[i]:
                start += 1
            else:
                end -= 1
    
    print(good)

n = int(input())

graph = sorted(list(map(int, input().split())))

binary(graph, n)
