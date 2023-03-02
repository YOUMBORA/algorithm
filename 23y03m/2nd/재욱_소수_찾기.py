from itertools import permutations as pt

def sosu(arr):
    result = 0
    n=max(arr)
    a = [False,False] + [True]*(n-1)

    for i in range(2,n+1):
        if a[i]:
            if i in arr:
                result += 1
            
            for j in range(2*i, n+1, i):
                a[j] = False
     
    return result

def solution(numbers):
    number = list(numbers)
    answer = 0
    cnt = 2
    list_ = number.copy()
    
    while True:
        if cnt > len(number):
            break
        
        for i in pt(number, cnt):
            s = i[0]
            for t in range(cnt-1):
                s += i[t+1]
            
            if s in list_:
                pass
            else:
                list_.append(s)
        cnt+=1
    
    int_list = list(set(map(int, list_)))
    
    return sosu(int_list)

