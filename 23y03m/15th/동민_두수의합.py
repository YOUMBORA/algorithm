def two_pointer_search(sorted_list, target):

    cur_min = abs(target - (sorted_list[0] + sorted_list[1]))

    start = 0
    end = len(sorted_list)-1
    cnt = 0
    while start < end:
        cur_sum = sorted_list[start]+sorted_list[end]
        delta = target - cur_sum
        if delta > 0: # target > cur_sum
            start += 1
        else: # target <= cur_sum
            end -= 1
        if abs(delta)<cur_min:
            cnt = 1
            cur_min = abs(delta)
        elif abs(delta)==cur_min:
            cnt += 1
        
    return cnt

test_cnt = int(input())
total_test = []

for i in range(test_cnt):
    N, target = map(int,input().split())
    temp_list = list(map(int, input().split()))
    total_test.append([N,target,temp_list])

for test in total_test:
    n,t,l = test
    sorted_l = sorted(l)
    result = two_pointer_search(sorted_l, t)
    print(result)
