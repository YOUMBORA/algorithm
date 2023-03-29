from bisect import bisect_left
import sys

input = sys.stdin.readline

def binary(n, A_list):
    cnt = 0

    for i in range(n-2):
        start = i+1
        end = n-1

        while start < end:

            hap = A_list[start] + A_list[end] + A_list[i]

            if hap > 0 :
                end -= 1

            else:
                if hap == 0:
                    if A_list[start] == A_list[end]:
                        cnt += (end - start)

                    else:
                        idx = bisect_left(A_list, A_list[end])
                        cnt += (end - idx + 1)
                
                start += 1
    
    print(cnt)

n = int(input())

A_list = sorted(list(map(int, input().split())))

binary(n, A_list)
