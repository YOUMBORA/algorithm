import sys

n,m = map(int, input().split())
num_list = list(map(int, input().split()))
result_list = []
sum_dict = {-1:0, 0:num_list[0]}

for j in range(1,n):
    sum_dict[j] = sum_dict[j-1] + num_list[j]
    
for i in range(m):
    start_id, end_id = map(int, sys.stdin.readline().split())
    result_list.append(sum_dict[end_id-1]-sum_dict[start_id-2])

for k in range(m):
    print(result_list[k])
