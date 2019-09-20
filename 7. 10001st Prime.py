primes = [2,3]
def primeChecker(num):
    for x in range(primes[len(primes)-1]+2,num,2):
        prime = True
        for y in range(2,num,1):
            if x%y == 0:
                prime = False
                break
            if y > x**1/2.0:
                break
        if prime == True:
            primes.append(x)
    prime = True
    for x in primes:
        if num%x == 0:
            prime = False
        if x > num**1/2.0:
            break
    return prime
            

def number():
    number = 0
    x = 3
    while True:
        x = x+2
        if primeChecker(x) == True:
            number = number + 1
            print(number)
            if number == 9999: '''prime target-2'''
                print(x)
                break

number()