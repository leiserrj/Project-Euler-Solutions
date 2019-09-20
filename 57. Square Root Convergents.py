def square():
    total = 0
    iterations = 4
    oldNum = 41
    oldDen = 29
    while iterations <= 1000:
        iterations = iterations + 1
        num = 2 * oldDen + oldNum
        den = oldDen + oldNum
        oldNum = num
        oldDen = den
        if len(str(num)) > len(str(den)):
            total = total + 1
    print(total)  
          
square()