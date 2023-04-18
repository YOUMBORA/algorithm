N = int(input())

def prime(n):
    for i in range(2,n):
        if not n%i:
            return False
    return True 
primes = []
queue = ['']
while queue:
    value = queue.pop()
    for i in range(10):
        new_value = value + str(i)
        if len(new_value) > N:
            break
        if prime(int(new_value)):
            if len(new_value) == N and int(new_value[0])>1:
                primes.append(new_value)
            queue.append(new_value)
primes.sort()
for p in primes:
    print(p)