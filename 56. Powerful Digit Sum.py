def power():
    total = 0
    for a in range(1,100):
        for b in range(1,100):
            digits = 0
            for x in range(len(str(a**b))):
                digits = digits + int(str(a**b)[x])
            if digits > total:
                total = digits
    print(total)
    
power()