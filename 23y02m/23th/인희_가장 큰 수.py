# 예를 들어, [3, 33, 303, 3033]이 있다고 할 때, 그냥 정렬을 하면 [33, 3033, 303, 3]이 된다. -> 3,330,333,033
# 하지만, 3,330,333,033 보다는 3,333,033,303 숫자가 더 크다. -> [33, 3, 3033, 303]
# 따라서, 문자열 정렬을 할 때, 뒤에 같은 문자열들을 3번 정도 붙여주며 정렬을 하자

def solution(numbers):
    answer = ''
    
    numbers.sort(key=lambda x: str(x)*3, reverse=True)

    for i in range(len(numbers)):
        answer += str(numbers[i])
    
    # test case : [0, 0, 0, 0] -> 0
    return str(int(answer)) 