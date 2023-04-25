N, M = map(int,input().split())
graph = list(map(int,input().split()))
s = max(graph)
e = sum(graph)
answer = 1e9

while s<=e:
    mid = (s+e)//2
    temp = 0
    count = 1
    for g in graph:
        temp += g 
        if temp > mid:
            temp = g
            count+=1
    if count > M:
        s= mid +1
    else:
        e = mid -1
        if mid >= max(graph):
            answer = min(answer,mid)

print(answer)