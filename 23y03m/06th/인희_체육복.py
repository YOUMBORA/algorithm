def solution(n, lost, reserve):
    answer = 0
    
    # 체육복을 가져온 학생이 도난당한 경우를 제외하고 list 재생성
    lost_lst = list(set(lost) - set(reserve))
    reserve_lst = list(set(reserve) - set(lost))
    
    # 체육복을 가져온 학생들 list를 기준으로, 앞 뒤 번호의 학생이 lost_lst에 존재하면 체육복 빌려주기
    for stu in reserve_lst:
        print(stu)
        if stu-1 in lost_lst:
            lost_lst.remove(stu-1)
        elif stu+1 in lost_lst:
            lost_lst.remove(stu+1)
    
    return n - len(lost_lst)