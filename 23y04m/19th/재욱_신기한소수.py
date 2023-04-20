import sys
from collections import deque

input = sys.stdin.readline

def isPrime(n, length):
    
    if len(str(n)) > length:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  
    return True

def bfs(length):
    queue = deque([2, 3, 5, 7])
    
    decimal = []

    while queue:
        x = queue.popleft()
        
        if len(str(x)) == length:
            if isPrime(x, length):
                decimal.append(x)
        x *= 10
        
        for i in range(10):
            cal = x + i
            
            if isPrime(cal, length):
                queue.append(cal)
        
    decimal.sort()
    for i in decimal:
        print(i)
    
bfs(int(input()))