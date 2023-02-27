def solution(jobs):
    answer = 0
    s = 0
    leng = len(jobs)
    
    jobs = sorted(jobs, key=lambda x: x[1])
    
    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0] <= s:
                s += jobs[i][1]
                answer += s - jobs[i][0]
                jobs.pop(i)
                break

            if i == len(jobs) - 1:
                s += 1
    
    return answer // leng
