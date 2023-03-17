n = int(input())
s = [int(input()) for _ in range(n)]

# 1 stair - 1
# 2 stair - 2 / 1,2
# 3 stair - 1,3 / 2,3
# 4 stair - 1,2,4 / 1,3,4 / 2, 4 
# 5 stair - 1,2,4,5 / 2,4,5 / 2,3,5 / 1,3,5

d =[0] *(n)
d[0] = s[0]
d[1] = max(s[1],s[0]+s[1])
for i in range(2, n):
    d[i] = max(d[i-3]+s[i-1]+s[i], d[i-2]+s[i])
print(d[-1])