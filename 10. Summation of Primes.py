def primeSum():
    primes = list(range(1000000))
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
    print(sum(primes))
    
primeSum()