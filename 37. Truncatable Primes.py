def trunc():
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
    
    total = 0
    for x in primes:
        if x > 10:
            trunc = True
            temp = str(x) 
            for y in range(len(str(x))-1):
                temp = temp[1:]
                if int(temp) not in primes:
                    trunc = False
                    break
            temp = str(x)
            if trunc == True:
                for y in range(len(str(x))-1):
                    temp = temp[:-1]
                    if int(temp) not in primes:
                        trunc = False
                        break
            if trunc == True:
                print(x)
                total = total + x
    print(total)
    
trunc()