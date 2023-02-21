# '('면 lst에 담고, ')'가 나왔을 때 lst의 마지막 부분이 '('라면 lst의 마지막 부분 삭제
# 최종적으로 lst에 아무 값도 없으면 True, 값이 존재하면 False

def solution(s):

    lst = []
    for bracket in s:
        if bracket == '(':
            lst.append(bracket)
        else:
            if lst[-1:] == ['(']:
                lst.pop()
            else:
                lst.append(bracket)

    if len(lst) == 0:
        return True
    else:
        return False