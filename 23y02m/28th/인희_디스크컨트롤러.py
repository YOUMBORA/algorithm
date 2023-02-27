import heapq

def solution(jobs):
    lens = len(jobs)
    answer = 0
    now = 0
    heap = []
    
    jobs.sort(key=lambda x: x[0])
    
    for i in range(lens):
        if jobs[0][0] == 0:
            now = jobs[0][1]
            answer += jobs[0][1]
            lst = jobs.pop(0)
            heap.append(lst)
            jobs.sort(key=lambda x: x[1])
        else:
            if now >= jobs[0][0]:
                jobs.sort(key=lambda x: x[1])
                answer += now - jobs[0][0] + jobs[0][1]
                now += jobs[0][1]
                lst = jobs.pop(0)
                heap.append(lst)
            else:
                jobs.sort(key=lambda x: x[1])
                answer += jobs[0][0] - now + jobs[0][1]
                now += jobs[0][1]
                lst = jobs.pop(0)
                heap.append(lst)
               
    return int(answer/lens)
