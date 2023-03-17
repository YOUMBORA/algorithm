t = int(input())
n = [int(input()) for _ in range(t)]

d = [0] * (max(n)+1)
# 1 - 1
# 2 - 1 + 1 / 2 
# 3 - 1 + 1 + 1 / 1 + 2 / 2 + 1 / 3 
d[1], d[2], d[3] = 1, 2, 4
for i in range(4, max(n)+1):
    d[i] = d[i-1] + d[i-2] + d[i-3]
for j in n:
    print(d[j])