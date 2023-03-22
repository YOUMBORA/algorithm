'''
나 : 2
case 1: 1이 2를 이겼어 ( 1 > 2 ) => 알고 있는 정보
case 2: 3이 2를 이겼어 ( 3 > 2 ) => ?? 연관성 찾기 어려움
case 3: 3이 2한테 졌어 ( 2 > 3 ) => 3은 1한테 질 수 밖에 없음

case 4: 1이 2한테 졌어 ( 2 > 1 ) => 알고 있는 정보
case 5: 3이 2를 이겼어 ( 3 > 2 ) => 3은 1을 이길 수 밖에 없음
case 6: 3이 2한테 졌어 ( 2 > 3 ) => ?? 연관성 찾기 어려움
'''

def solution(n, results):
    
    # 얘네(index에 있는 원소)가 날(index) 이겼어
    win = [set() for _ in range(n+1)]
    # 얘네(index에 있는 원소)는 나한테(index) 졌어
    lose = [set() for _ in range(n+1)]
    
    # 나한테 이긴 list와 나한테 진 list를 만들어주기
    for a, b in results:
        win[b].add(a)
        lose[a].add(b)
    
    # 알고 있는 정보를 가지고 위 case에 맞게 확실한 정보를 list에 각각 추가해주기
    for i in range(1, n+1):
        for winner in win[i]:
            lose[winner].update(lose[i])
        for loser in lose[i]:
            win[loser].update(win[i])
    
    # 정확하게 순위를 매길 수 있는 경우의 수를 찾기
    answer = 0
    for j in range(1, n+1):
        ans = len(win[j]) + len(lose[j])
        if ans == (n-1):
            answer += 1

    return answer