N, C = map(int, input().split())
graph = [int(input()) for _ in range(N)]
graph.sort()

s = 1
e = graph[-1]-graph[0]

answer = 0

while s<=e:
    mid = (s+e)//2
    cur = graph[0]
    count = 1

    for i in range(1, len(graph)):
        if graph[i] >= cur + mid:
            count += 1
            cur = graph[i]
    if count >= C:
        answer = mid 
        s = mid+1
    else:
        e = mid-1

print(answer)