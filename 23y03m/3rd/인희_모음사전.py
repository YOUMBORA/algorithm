# product => 중복 순열 라이브러리
# 참고 : https://velog.io/@insutance/Python-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC
from itertools import product

def solution(word):
    answer = 0
    
    word_list = []
    # 길이가 1부터 5까지 존재하는 알파벳들의 중복순열 구하기
    for i in range(1, 6):
        for j in list(product(['A', 'E', 'I', 'O', 'U'], repeat=i)):
            word_list.append(''.join(j))
    # 모음사전은 정렬 오름차순 순서로 되어 있음
    word_list.sort()
    
    return word_list.index(word) + 1