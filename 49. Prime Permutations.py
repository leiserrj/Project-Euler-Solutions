def perms():
    primes = list(range(10000))
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
    
    for x in primes:
        if len(str(x)) != 4:
            continue
        digits = []
        for y in str(x):
            if y not in digits:
                digits.append(int(y))
        tempdigits = digits
        perms = []
        for a in tempdigits:
            tempdigits.remove(a)
            for b in tempdigits:
                tempdigits.remove(b)
                for c in tempdigits:
                    tempdigits.remove(c)
                    for d in tempdigits:
                        tempdigits.remove(d)
                        if len(str(int(str(a)+str(b)+str(c)+str(d)))) == 4:
                            perms.append(str(a)+str(b)+str(c)+str(d))
                        tempdigits.append(d)
                    tempdigits.append(c)
                tempdigits.append(b)
            tempdigits.append(a)
        perms = sorted(perms)
        
        for a in perms:
            if x >= int(a):
                continue
            if str(int(a)+3330) in perms and int(a) in primes and int(a)+3330 in primes and int(a)-x == 3330:
                print(str(x)+a+str(x+6660))
                break
                    

perms()