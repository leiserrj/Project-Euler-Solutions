def trip():
    for a in range(1,499,1):
        for b in range(501-a,999-a,1):
            c = ((a**2)+(b**2))**(1/2.0)
            if a+b+c == 1000:
                print(a*b*c)
                print([a,b,c])
                return 1

trip()