def powerDigit():
    num = 2**1000
    total = 0
    for x in range(len(str(num))):
        total = total + int(str(num)[x])
    print(total)
    
powerDigit()