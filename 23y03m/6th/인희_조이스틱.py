# 상하로 알파벳 이동하기(최소값)
def updown(alpha):
    return min(ord('Z') - ord(alpha) + 1, ord(alpha) - ord('A'))


def solution(name):
    answer = 0
    
    # 커서를 왼쪽으로 이동시킬지 오른쪽으로 이동시킬지 결정하기(연속된 A가 얼마나 나타나는지 확인)
    left = 0
    right = 0
    for i in range(1, len(name)):
        if name[i] == 'A':
            right += 1
        if name[-i] == 'A':
            left += 1
        else:
            break

    answer += updown(name[0])

    if left >= right:
        answer += len(name) - left - 1
        for i in range(1, len(name)):
            answer += updown(name[i])
    else:
        answer += len(name) - right - 1
        for i in range(1, len(name)):
            answer += updown(name[i])    
    
    return answer