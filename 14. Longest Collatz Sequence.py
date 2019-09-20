def collatz():
    long = 0
    longStart = 0
    
    for x in range(2,1000000,1):
        print(x)
        start = x
        steps = 0
        while x != 1:
            if x%2 == 0:
                x = x/2
            else:
                x = 3*x+1
            steps = steps + 1
        if steps > long:
            long = steps
            longStart = start
            
    print(long)
    print(longStart)
    
collatz()