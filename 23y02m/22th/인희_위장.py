from collections import Counter

def solution(clothes):
    
    # 의상의 종류마다 개수 세기
    cloth_type = []
    for type in clothes:
        cloth_type.append(type[1])
    
    wear = Counter(cloth_type)
    
    # 아무것도 안 입는 경우의 수를 의상 종류마다 추가하여 곱하고, 마지막에 아무 것도 입지 않는 경우를 빼기
    cnt = 1
    for j in wear:
        cnt *= wear[j] + 1
    
    return cnt - 1