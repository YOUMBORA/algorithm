def solution(progresses, speeds):
    answer = []
    if len(progresses) == len(speeds):
        work_days = []
        for idx, prog in enumerate(progresses):
            work_float = (100-prog)/speeds[idx]
            work_int = (100-prog)//speeds[idx]
            if work_float > work_int:
                work_days.append(work_int+1)
            else:
                work_days.append(work_int)
        w_stack = []
        for w in work_days:
            if w_stack == []:
                w_stack.append(w)
            else:
                if w_stack[0] >= w :
                    w_stack.append(w)
                else:
                    answer.append(len(w_stack))
                    w_stack = []
                    w_stack.append(w)
        answer.append(len(w_stack))
    else:
        return False
    return answer