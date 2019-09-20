def chains():
    total = 0
    for x in range(1,10000000):
        print(x)
        result = x
        while True:
            temp = 0
            for y in str(result):
                temp = temp + (int(y)**2)
            result = temp
            if result == 89:
                total = total + 1
                break
            elif result == 1:
                break
    print(total)
    
chains()