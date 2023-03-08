def solution(answers):
    supo_1 = list(range(1,6))
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = [0,0,0]
    for idx,val in enumerate(answers):
        if supo_1[idx%5] == val:
            answer[0] += 1
        if supo_2[idx%8] == val:
            answer[1] += 1
        if supo_3[idx%10] == val:
            answer[2] += 1
    ans  = [ idx + 1 for idx,val in enumerate(answer) if val == max(answer)]


    return ans

if __name__ == '__main__':
    answers = [1,2,3,4,5]
    print(solution(answers))
    answers = [1,3,2,4,2]
    print(solution(answers))