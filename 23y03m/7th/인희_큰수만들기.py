######################## 시간 초과 ^^ ############################
from itertools import combinations

def solution(number, k):
    lst = []
    for i in list(combinations(number, len(number)-k)):
        lst.append(''.join(i))
    lst.sort(reverse = True)

    return lst[0]
#################################################################

############################# 성공 ##############################

# stack을 이용하여 풀기

def solution(number, k):

    stack = []
    for num in number:
        # 더 이상 제거할 수 있는 경우 X, stack이 빈 경우, 더 쌓을 값보다 stack의 마지막 값이 작다면 pop계속 해주기
        while k > 0  and len(stack) != 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
        
    # test case 12 : number -> "4321", k -> "1", return -> "432"
    return ''.join(stack[:len(stack)-k])
#################################################################
