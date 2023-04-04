import sys
import math
input = sys.stdin.readline

# 입력 받기
n, H = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

# 던전에 들어가자
def dungeon(H, hp, room):
    now_hp = hp
    for t, a, h in room:
        # 용사의 체력이 0 이하이면 전투가 종료되고, 용사는 사망한다.
        if now_hp <= 0:
            return False
        
        # 몬스터가 있는 방일 때
        if t == 1:
            soldier_win = math.ceil(h / H)
            soldier_lose = math.ceil(now_hp / a)
            # 용사가 몬스터와 싸운 후 그만큼의 체력을 깎는다.
            if soldier_win <= soldier_lose:
                now_hp -= (a * (soldier_win-1))
            # 용사의 체력이 0 이하이면 전투가 종료되고, 용사는 사망한다.
            else:
                return False
        # 포션이 있는 방일 때
        else:
            H += a
            # 용사의 최대 체력만큼만 회복 가능하다.
            if (now_hp + h) <= hp:
                now_hp += h
            else:
                now_hp = hp

    return True

### 주의@@@!!! : 용사의 최대 생명력은 (방의 최대 개수 * 용사의 최대 초기 공격력 * 몬스터의 최대 공격력) => 이 부분을 너무 높게 잡아서 시간 초과가 났음!!ㅜㅜ
start_hp = 1
end_hp = 1123456 * 1000000 * 1000000
answer = 0

# 이분탐색 시작
while start_hp <= end_hp:
    mid_hp = (start_hp + end_hp) // 2

    if dungeon(H, mid_hp, room):
        end_hp = mid_hp - 1
        answer = mid_hp
    else:
        start_hp = mid_hp + 1
        
print(int(answer))