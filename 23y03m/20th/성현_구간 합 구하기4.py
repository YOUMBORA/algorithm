n, m = map(int,input().split())
n_list = list(map(int,input().split()))
d = [0]*(n+1)
d[0] = 0
d[1] = n_list[0]
for i in range(1,n):
    d[i+1] = n_list[i] +d[i]
for _ in range(m):
    s, e = map(int,input().split())
    print(d[e]-d[s-1])
