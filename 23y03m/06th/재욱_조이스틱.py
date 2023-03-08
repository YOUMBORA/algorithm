def solution(name):
    answer = 0
    length = len(name)
    next_idx = 0
    
    for idx, char in enumerate(name):

        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next_idx = idx + 1

        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1 
        
        length = min(length, idx + idx + len(name) - next_idx, idx + 2 * (len(name) - next_idx))
        # length = min(length, idx + idx + len(name) - next_idx)
        # min(기존 방식 / A 문자열 까지(idx) + 다시 왼쪽으로 진행(idx + len(name)-next)
        # A 문자열 까지(len(name)-next) + 다시 오른쪽으로 진행(len(name)-next + idx)
        # idx + 2 * (len(name) - next_idx) < 부분 답안지 
        
    answer += length
    return answer

print(solution("BBAAABAAAAAAAAAAAABA"))
