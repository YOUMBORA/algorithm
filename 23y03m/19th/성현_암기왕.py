t = int(input())
for _ in range(t):
    n = int(input())
    n_list = list(map(int,input().split()))
    m = int(input())
    m_list = list(map(int,input().split()))
    n_list.sort()
    for x in m_list:
        start = 0
        end = n-1
        answer = 0
        while start <= end:
            mid = (start+end)//2
            if n_list[mid] == x:
                answer = 1
                break
            elif n_list[mid] < x:
                start = mid+1
            else:
                end = mid-1
        print(answer)