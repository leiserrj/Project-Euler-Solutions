def power():
    total = 0
    for x in range(1,100):
        test = 1
        while True:
            if len(str(test**x)) > x:
                break
            if len(str(test**x)) == x:
                print(x)
                print(test**x)
                total = total + 1
            test = test + 1
    print(total)
    
power()