# 입력 받기(하루동안 본 정수를 set으로 씌워주기)
T = int(input())
for i in range(T):
    n = int(input())
    note1 = set(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    # note2에 있는 숫자가 note1에 있다면 1, 아니면 0 출력
    for j in note2:
        if j in note1:
            print(1)
        else:
            print(0)
