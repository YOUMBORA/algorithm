import sys

input = sys.stdin.readline

def binary_search(target, find_list):
    
    start = 0
    end = len(find_list) -1
    
    while start <= end:
        mid = (start + end) // 2
        
        if find_list[mid] == target:
            return 1

        elif find_list[mid] > target:
            end = mid - 1

        else:
            start = mid + 1
            
    return 0


T = int(input())

for _ in range(T):
    n = int(input())
    find_list = sorted(list(map(int, input().split())))
    
    m = int(input())
    find = list(map(int, input().split()))
    
    for i in find:
        print(binary_search(i, find_list))
