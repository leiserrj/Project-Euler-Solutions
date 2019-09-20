def recip():
    most = 0
    mostL = 0
    for x in range(7,1000):
        print(x)
        digit = 1
        digits = []
        while digit not in digits or digits == []:
            digits.append(digit)
            digit = digit *10
            digit = digit % x
            if digit == 0:
                break
            print(digit)
        for y in range(len(digits)):
            if digit == digits[y]:
                if len(digits)-y > most:
                    most = len(digits)-y
                    mostL = x
                    
    print(mostL)
    
recip()