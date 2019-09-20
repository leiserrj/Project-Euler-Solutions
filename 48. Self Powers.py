def pows():
    total = 0
    for x in range(1,1001):
        total = total + x**x 
        print(x)
    print(str(total)[-10:])
    
pows()