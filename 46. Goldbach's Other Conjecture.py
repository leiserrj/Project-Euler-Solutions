def gold():
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
    
    num = 33
    while True:
        num = num + 2
        if num in primes:
            continue
        for a in range(1,int(((num-2)/2)**.5)+1):
            if num - 2*(a**2) in primes:
                break
        else:
            print(num)
            break
        
gold()