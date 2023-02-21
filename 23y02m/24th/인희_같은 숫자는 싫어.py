# 신기한 아이디어 : 빈 list에서 print(list[-1:])를 하더라도 빈 리스트가 출력됨

def solution(arr):
    answer = []
    
    for num in arr:
        if len(answer) == 0:
            answer.append(num)
        else:
            # 연속적으로 나타나는 숫자면 pass
            if num == answer[-1]:
                continue
            else:
                answer.append(num)

    return answer