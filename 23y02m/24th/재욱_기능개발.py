import math
def solution(progresses, speeds):
    answer = []
    result = []
    if len(progresses) == 1:
        return [1]

    for progress, speed in zip(progresses, speeds):
        answer.append(math.ceil(((100 - progress) / speed)))

    count = 1

    for idx in range(1, len(answer)):
        if idx == (len(answer) - 1):
            if answer[idx-count] >= answer[idx]:
                result.append(count+1)
            else:
                result.append(count)
                result.append(1)
        elif answer[idx-count] >= answer[idx]:
            count += 1
        else:
            result.append(count)
            count = 1
    return result
