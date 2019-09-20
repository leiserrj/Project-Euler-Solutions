def circular():
    total = 0
    primes = list(range(500000))
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
    print(primes)
    
    result = []
    nons = []
    
    for x in primes:
        for y in str(x):
            if int(y)%2 == 0 and x != 2:
                nons.append(x)
            if int(y) == 5:
                nons.append(x)
        if x not in result and x not in nons:        
            prime = True
            perm = str(x)
            temp = []
            if x > 9:
                for y in range(len(str(x))):
                    perm = perm[1:]+perm[0]
                    if int(perm) not in primes:
                        temp.append(perm)
                        prime = False
                        break
            if prime == True:
                result.append(temp)
                print(x)
        elif x not in nons:
            result.append(x)
            print(x)
            
    print(len(result)+1)
    
circular()