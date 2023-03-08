def solution(answers):
    answer = answers
    leng_ = len(answer)
    a = [1, 2, 3, 4, 5] * 2000
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    a = a[:leng_+1]
    b = b[:leng_+1]
    c = c[:leng_+1]

    result = [0, 0, 0]

    for ans, rs, rs1, rs2 in zip(answer, a, b, c):
        if ans == rs:
            result[0] += 1
        if ans == rs1:
            result[1] += 1
        if ans == rs2:
            result[2] += 1

    RANK = [1, 2, 3]
    result_ = []

    for i in range(len(result)):
        if result[i] == max(result):
            result_.append(RANK[i])

    return result_
