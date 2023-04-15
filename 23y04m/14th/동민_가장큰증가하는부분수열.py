import sys

N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
graph = num_list[:]
result = graph[:]

for i in range(1, N):
    for j in range(i):
        if graph[j] < graph[i]:
            result[i] = max(result[i], result[j] + graph[i])

print(max(result))
