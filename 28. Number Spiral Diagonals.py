def spiral():
    total = 1
    num = 1
    for x in range(500):
        for y in range(4):
            num = num + (x+1)*2
            total = total + num 
    print(total)
    
spiral()