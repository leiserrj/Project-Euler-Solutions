def primeList(num):
    '''creates a list of all primes up to num*2+1'''
    primes = list(range(num))
    primes = list(map(lambda x:x*2+1,primes))
    primes[0] = 2
    
    for x in range(1,len(primes),1):
        for y in range(0,len(primes),1):
            if primes[y] != 0:
                if primes[x]%primes[y] == 0:
                    primes[x] = 0
                    break
                if primes[y] > primes[x]**0.5:
                    break
    primes = list(filter(lambda x: x != 0,primes))
    return primes
def isPrime(num,primeList):
    for x in primeList:
        if x > num**(1/2):
            return True
        if num % x == 0:
            return False
        
primeList = primeList(500000)
num = 1
increment = 0
primes = 0
total = 0
while True:
    increment += 2
    for x in range(4):
        num += increment
        total += 1
        if isPrime(num,primeList):
            primes += 1
        if 10*primes < total:
            print(increment-1)
            sys.exit(0)
    