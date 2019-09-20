def quad():
    most = 0
    mostA = 0
    mostB = 0
    primes = [2,3]
    for a in range(-1000,1000):
        for b in range(0-a-1,1001):
            numPrimes = 0
            number = 0
            result = 2
            while result in primes:
                number = number + 1
                result = (number**2) + (a*number) + b
                if primes[-1] < result:
                    for x in range(primes[-1]+2,result + 1,2):
                        for y in primes:
                            if x%y == 0:
                                break
                            if y > x**0.5:
                                primes.append(x)
                                break
                if result in primes:
                    numPrimes = numPrimes + 1
            if numPrimes > most:
                most = numPrimes
                print(most)
                mostA = a
                print(a)
                mostB = b
                print(b)
    print(mostA*mostB)
    
quad()