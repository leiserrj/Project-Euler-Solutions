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

while True:
    primes = primeList(500000)
    for prime in primes:
        print(prime)
        digits0 = []
        digits1 = []
        digits2 = []
        for x in range(len(str(prime))):
            if str(prime)[x] == '0':
                digits0.append(x)
            if str(prime)[x] == '1':
                digits1.append(x)
            if str(prime)[x] == '2':
                digits2.append(x)
        if len(digits0) != 0:
            correct = 0
            for a in range(10):
                temp = str(prime)
                for b in digits0:
                    temp = temp[:b] + str(a) + temp[b+1:]
                if int(temp) in primes and temp[0] != '0':
                    correct += 1
                    if correct == 8:
                        print(prime)
                        sys.exit(0)
        if len(digits1) != 0:
            correct = 0
            for a in range(10):
                temp = str(prime)
                for b in digits1:
                    temp = temp[:b] + str(a) + temp[b+1:]
                if int(temp) in primes and temp[0] != '0':
                    correct += 1
                    if correct == 8:
                        print(prime)
                        sys.exit()
        if len(digits2) != 0:
            correct = 0
            for a in range(10):
                temp = str(prime)
                for b in digits2:
                    temp = temp[:b] + str(a) + temp[b+1:]
                if int(temp) in primes and temp[0] != '0':
                    correct += 1
                    if correct == 8:
                        print(prime)
                        sys.exit(0)
        