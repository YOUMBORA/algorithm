N, M = map(int,input().split())

parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1,v2):
    r1 = find(v1)
    r2 = find(v2)

    if rank[r1] > rank[r2]:
        parent[r2] = r1
    else:
        parent[r1] = r2
        if rank[r1] == rank[r2]:
            rank[r2] += 1

for i in range(N+1):
    make_set(i)

for i in range(M):
    u, v = map(int,input().split())
    if find(u) != find(v):
        union(u,v)

ans = set()
for i in range(1, N+1):
    ans.add(find(i))

print(len(ans))
