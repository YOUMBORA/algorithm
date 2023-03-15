### 시간초과, 이분탐색으로 구현을 어떻게 할 지 모르곘음
import sys
from collections import Counter

input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    
    n_list = list(map(str, input().strip()))
    max_ = 0
    
    for i in range(len(n_list)):
        start = i
        end = i + n
        while end < len(n_list)-1:           
            x = Counter(n_list[i:end+1])
            
            if len(x) > n:
                break
            
            max_ = max(max_, sum(x.values()))
            
            end += 1
            
    print(max_)
    
