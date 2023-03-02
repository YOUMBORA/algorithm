def solution(answers):
    answer = []
    correct_count = [0]*3
    math_1 = [1,2,3,4,5]
    math_2 = [2,1,2,3,2,4,2,5]
    math_3 = [3,3,1,1,2,2,4,4,5,5]
    
    for idx, ans in enumerate(answers):        
        if ans == math_1[idx%len(math_1)]:
            correct_count[0]+=1   
        if ans == math_2[idx%len(math_2)]:
            correct_count[1]+=1
        if ans == math_3[idx%len(math_3)]:
            correct_count[2]+=1
            
    for i in range(3):
        if correct_count[i]==max(correct_count):
                answer.append(i+1)
    return answer