def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        n = 0
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                print(prices[i], prices[j])
                n += 1
                break
            else:
                n += 1
            
        answer.append(n)
            
    return answer