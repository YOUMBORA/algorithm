import sys 

input = lambda : sys.stdin.readline().strip()

N, A = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def can_clear(curATK, maxHP):
    curHP = maxHP
    for ty, atk, hp in graph:
        if ty == 1:
            turn = hp//curATK if not hp%curATK else hp//curATK+1
            curHP -= atk * (turn-1)
        else:
            curATK += atk 
            curHP += hp 
            if curHP > maxHP:
                curHP = maxHP 
        if curHP <= 0:
            return False 
    return True 

result = 0
l, r = 1, int(1e6*1e6)

while l <= r:
    mid = (l+r)//2
    if can_clear(A,mid):
        r = mid -1
        result = mid 
    else:
        l = mid +1
print(result)
