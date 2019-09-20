def double():
    total = 0
    for x in range(1,1000000,2):
        binary = int(bin(x)[2:])
        pal = True
        for y in range(len(str(x))):
            if str(x)[y] != str(x)[-y-1]:
                pal = False
            if y > len(str(x))/2:
                break
            
        if pal == True:
            for y in range(len(str(binary))):
                if str(binary)[y] != str(binary)[len(str(binary))-y-1]:
                    pal = False
                if y > len(str(binary))/2:
                    break
                
        if pal == True:
            total = total + x
    print(total)        
double()