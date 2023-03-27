import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
num.sort()

def one_mean(n, num):
    return round(sum(num) / n)

def two_median(n, num):
    return num[n//2]

def three_mode(n, num):
    number = Counter(num).most_common(2)
    
    if len(number) == 1:
        return number[0][0]
    else:
        if number[0][1] != number[1][1]:
            return number[0][0]
        else:
            return number[1][0]

def four_range(n, num):
    return num[-1] - num[0]

print(one_mean(n, num))
print(two_median(n, num))
print(three_mode(n, num))
print(four_range(n, num))