def solution(numbers, target):

    # for문을 돌면서 숫자를 더해주거나 빼주는 과정을 lst에 계속해서 담아주기
    lst = [0]
    for number in numbers:
        tmp = []
        for num in lst:
            tmp.append(num + number)
            tmp.append(num - number)
        lst = tmp
    
    # target과 일치하는 원소의 개수만 return하기
    return lst.count(target)