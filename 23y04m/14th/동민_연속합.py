import sys

N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
graph = num_list[:]

for i in range(1, N):
    graph[i] = max(graph[i], graph[i - 1] + graph[i])

print(max(graph))
