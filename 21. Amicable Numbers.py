def amicable():
    numbers = []
    for x in range(2,10000,1):
        factors = []
        factors2 = []
        if x not in numbers:
            for y in range(1,int((x/2)+1),1):
                if y > x/2:
                    break
                if x%y == 0:
                    factors.append(y)
            if sum(factors) not in numbers:
                for y in range(1,int((sum(factors)/2)+1),1):
                    if y > sum(factors)/2:
                        break
                    if sum(factors)%y == 0:
                        factors2.append(y)
            if x == sum(factors2) and x != sum(factors):
                numbers.append(x)
                numbers.append(sum(factors))
    print(sum(numbers))
    
amicable()