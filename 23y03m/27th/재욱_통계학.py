import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

cal_list = sorted([int(input()) for _ in range(n)])
count_list = Counter(cal_list).most_common(2)

print(round(sum(cal_list) / n))
print(cal_list[n//2])

if len(count_list) > 1:
    if count_list[0][1] == count_list[1][1]:
        print(count_list[1][0])

    else:
        print(count_list[0][0])
else:
    print(count_list[0][0])
    
print(cal_list[-1] - cal_list[0])