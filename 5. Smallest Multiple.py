def smallM():
    num = 0
    while True:
        num = (2*3*5*7*11*13*17*19) + num
        print(num)
        check = True
        for x in range(20):
            if num%(x+1) != 0:
                check = False
                break
        if check == True:
            print("TRUE")
            break
            return num 
        
smallM()