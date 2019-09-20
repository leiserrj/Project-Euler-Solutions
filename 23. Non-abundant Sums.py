def abundant():
    sum = 20437
    abundants = []
    for x in range(12,20162,1):
        factorSum = 1
        for y in range(2,int(x/2)+1,1):
            if x%y == 0:
                factorSum = factorSum + y
        if factorSum > x:
            abundants.append(x)
    for x in range(24,20162,1):
        print(x)
        for y in abundants:
            if y > x:
                sum = sum + x
                break
            if x-y in abundants:
                print('yes')
                break
    print(sum)
    
abundant()