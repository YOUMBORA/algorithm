def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        slice = array[i-1:j]  # 조건 1
        slice.sort()  # 조건 2
        answer.append(slice[k-1])  # 조건 3
    
    return answer