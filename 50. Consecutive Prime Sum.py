def consec():
    primes = list(range(499999))
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
    
    most = 0
    biggest = 0
    
    for x in range(len(primes)):
        total = primes[x]
        term = 1
        while total < 1000000 and x+term < len(primes):
            total = total + primes[x+term]
            if term + 1 > most and total in primes:
                most = term + 1
                biggest = total
            term = term + 1
    print(biggest)
    
consec()