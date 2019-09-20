def sumS():
    sTotal = 0
    total = 0
    for x in range(101):
        sTotal = sTotal + x*x 
        total = total + x
    print(total*total - sTotal)

sumS()