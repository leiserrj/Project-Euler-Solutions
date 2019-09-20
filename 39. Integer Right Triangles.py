def triangles():
    most = 0
    mostP = 0
    
    for p in range(4,1001):
        num = 0
        for a in range(1,int(p/2)+1):
            for b in range(1,int(p/2)+1):
                c = p-a-b
                if c**2 == a**2 + b**2:
                    num = num + 1
        if num > most:
            most = num 
            mostP = p
    print(most)
    print(mostP)

triangles()