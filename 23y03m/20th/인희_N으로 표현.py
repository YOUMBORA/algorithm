# test case 5, 6, 7, 8 fail

def solution(N, number):

    answer = [0, [N]]
    
    if N == number:
        return 1

    for i in range(2, 9):
        dp = []
        dp.append(int(str(N)*i))
        
        for j in range(len(answer[-1])):
            plus = answer[-1][j] + N
            minus1 = answer[-1][j] - N
            minus2 = N - answer[-1][j]
            multi = answer[-1][j] * N
            div1 = answer[-1][j] // N
            
            if answer[-1][j] != 0:
                div2 = N // answer[-1][j]
                dp.append(div2)
                
            dp.append(plus)
            dp.append(minus1)
            dp.append(minus2)
            dp.append(multi)
            dp.append(div1)
        
        if number in dp:
            return i
        
        answer.append(list(set(dp)))
        print(answer)
    return -1