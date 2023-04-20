# from collections import Counter as ct
# N = int(input())

# N_list = ct(map(int, input().split()))

# M = int(input())
# M_list = list(map(int, input().split()))

# for i in M_list:
#     if i in N_list.keys():
#         print(1)
#     else:
#         print(0)
        
import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())

N_list = sorted(list(map(int, input().split())))

M = int(input())

M_list = list(map(int, input().split()))

for i in M_list:
    x = bisect_left(N_list, i)
    try:
        if i == N_list[x]:
            print(1)
        else:
            print(0)
    except:
        # print(i, x)
        print(0)