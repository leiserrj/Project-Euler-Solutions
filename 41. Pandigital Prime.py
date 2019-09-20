def pan():
    primes = list(range(int(2768/2)))
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
    
    for x in range(7654321,0,-2):
        prime = True
        for z in primes:
            if x%z == 0:
                prime = False
                break
        digit = list(range(len(str(x))))
        digit = list(map(lambda x: x+1,digit))
        numbers = []
        for y in str(x):
            numbers.append(int(y))
        numbers = sorted(numbers)
        if digit == numbers and prime == True:
            print(x)
            break
        
pan()