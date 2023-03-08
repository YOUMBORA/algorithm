
# 2 ~ n-1 까지 나누기
def isPrime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

# 2 ~ n/2 까지 나누기
def isPrime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False  
    return True

# 2 ~ \sqrt{n} 까지 나누기
def isPrime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False  
    return True
  

# 에라토스테네스의 체
def primeList(n):
	a = [False,False] + [True]*(n-1)
	primes=[]

	for i in range(2,n+1):
	  if a[i]:
	    primes.append(i)
	    for j in range(2*i, n+1, i):
	        a[j] = False
                
    return primes
