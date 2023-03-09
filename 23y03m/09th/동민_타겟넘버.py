def solution(numbers,target):

    a_list = []
    b_list = []
    def dfs():

        if len(a_list) == len(numbers):
            b_list.append(a_list[:])
            return
        else:
            for i in range(-1,2,2):
                a_list.append(i)
                dfs()
                a_list.pop()
    dfs()
    cnt = 0
    for i in b_list:
        if sum([numbers[j]*i[j] for j in range(len(i))]) == target:
            cnt+= 1
    return cnt
