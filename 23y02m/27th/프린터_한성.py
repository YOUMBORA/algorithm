def solution(priorities, location):
    answer =0
    # location은 몇번째 순서로 나오는지 궁금한 위치
    # priorities는 우선순위가 담긴 배열
    # 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
    # 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
    # 3. 그렇지 않으면 J를 인쇄합니다.
    arr = [(idx,val) for idx, val in enumerate(priorities)]
    print(arr)
    while True:
        tmp = arr.pop(0)
        print(tmp)
        if any(tmp[1] < i for _,i in arr):
            arr.append(tmp)
            print('prio : ',arr)
        else:
            answer += 1
            if tmp[0] == location:
                return answer



if __name__ == '__main__':
    a = [2, 1, 3, 2]
    b = 2
    print(solution(a,b))
    a = [1, 1, 9, 1, 1, 1]
    b = 0
    print(solution(a,b))