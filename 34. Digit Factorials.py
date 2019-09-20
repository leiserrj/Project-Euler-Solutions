def fact():
    total = 0
    for x in range(10,40586,1):
        temp = 0
        for y in range(len(str(x))):
            fact = 1
            if str(x)[y] != '0':
                for z in range(1,int(str(x)[y])+1,1):
                    fact = fact * z
            temp = temp + fact
        if temp == x:
            total = total + temp
    print(total)
    
fact()