from collections import Counter
N = int(input())

xl = []
for i in range(N):
    xl.append(int(input()))
mx = sum(xl)/len(xl)
dx = sum(xl)//len(xl)

if mx != dx:
    if mx > 0:
        if abs((mx*10)%10) >= 5:
            print(dx+1)
        else:
            print(dx)
    else:
        if abs((mx*10)%10) < 5:
            print(dx)
        else:
            print(dx+1)
else:
    print(dx)

print(sorted(xl)[len(xl)//2])

mc = Counter(sorted(xl)).most_common(2)
if len(xl) > 1:
    if mc[0][1] == mc[1][1]:
        print(mc[1][0])
    else:
        print(mc[0][0])
else:
    print(mc[0][0])

print(sorted(xl)[-1]-sorted(xl)[0])