def binary(m,sa,ka):
    answer= 0
    value = 1e9
    for i in range(m):
        start = i+1
        end = n-1
        while start<=end:
            mid = (start+end)//2
            avg = sa[i] + sa[mid]
            if avg > ka:
                end = mid -1
            else:
                start = mid +1
            if abs(avg-ka) < value:
                answer = 1
                value = abs(avg-ka)
            elif abs(avg-ka) == value:
                answer +=1
    return answer

t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    s = [i for i in map(int,input().split())]
    s.sort()
    print(binary(n,s,k))