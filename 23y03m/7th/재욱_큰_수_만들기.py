def solution(number, k):
    num = list(number)
    length = len(number) - k
    cnt = 0  

    while True:
        if k == 0 or length == len(num):
            break

        try:
            if num[cnt] < num[cnt+1]:
                del num[cnt]
                if cnt - k >= 0:
                    cnt -= k
                else:
                    cnt = 0
                k -= 1
            else:
                cnt +=1
        except:
            answer = ''.join(num[:length])
            return answer

    answer = ''.join(num)
    return answer
