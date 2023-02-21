import math

def solution(progresses, speeds):
    answer = []
    
    # 며칠 후 배포 가능한지 lst에 담기
    lst = []
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        days = remain / speeds[i]
        lst.append(math.ceil(days))

    # 배포 가능한 최대 날짜를 today로 설정하고, 몇 개의 기능을 배포할지(cnt) 정하기
    today = lst[0]
    cnt = 1
    for j in range(1, len(lst)):
        if lst[j] <= today:  
            cnt += 1
        else:
            answer.append(cnt)
            today = lst[j]
            cnt = 1
    answer.append(cnt)
            
    return answer