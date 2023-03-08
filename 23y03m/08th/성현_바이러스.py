import sys 

input = lambda : sys.stdin.readline().strip()

parent = {}
rank = {}

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    r1 = find(u)
    r2 = find(v)

    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r1] = r2
        else:
            parent[r2] = r1
            if rank[r1] == rank[r2]:
                rank[r2]+=1

def make_set(node):
    parent[node] = node 
    rank[node] = 0 

computer = int(input())
numbers = int(input())

for i in range(1, computer+1):
    make_set(i)

for i in range(numbers):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a,b)
        
answer = 0 
for i in range(1, computer+1):
    if find(i) == parent[1]:
        answer += 1
print(answer-1)