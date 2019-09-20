def largestPrime(num):
    largest = 0
    for x in range(num-1):
        if num%(x+1) == 0:
            prime = True
            for y in range(x):
                if (x+1)%(y+1) == 0 and y != 0:
                    prime = False
            if prime == True:
                largest = x+1
                print(largest)
    
largestPrime(600851475143)