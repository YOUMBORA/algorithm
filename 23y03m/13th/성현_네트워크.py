parent ={}
rank ={}

def make_set(n):
    for i in range(n):
        parent[i]=i
        rank[i]=0
        
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(a,b):
    r1 = find(a)
    r2 = find(b)
    
    if rank[r1] > rank[r2]:
        parent[r2] = r1
    else:
        parent[r1] = r2 
        if rank[r1] == rank[r2]:
            rank[r2] +=1
            
def solution(n, computers):
    make_set(n)
    for i in range(n):
        for j in range(n):
            if find(i) != find(j):
                if computers[i][j] == 1:
                    union(i,j)
    return len(set(parent.values()))