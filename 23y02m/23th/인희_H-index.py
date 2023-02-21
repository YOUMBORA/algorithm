# 논문 : [15, 12, 10, 8, 6, 3, 2, 1]
# index : [0, 1, 2, 3, 4, 5, 6, 7]
# 인용된 수가 적힌 논문들이 내림차순으로 배열되면,
# index number에 대입하여 index가 더 클 때 반환

# test case 11 : [100, 100, 100] -> 3
# test case 16 : [0, 0, 0, 0, 0] -> 0

def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    print(citations)
    
    for idx in range(len(citations)):
        if idx >= citations[idx]:
            return idx
        
    return len(citations)