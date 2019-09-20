def comb():
    total = 0
    for n in range(2,101):
        for r in range(1,n):
            top = 1
            bottom1 = 1
            bottom2 = 1
            for a in range(1,n+1):
                top = top * a 
            for b in range(1,r+1):
                bottom1 = bottom1 * b 
            for c in range(1,n-r+1):
                bottom2 = bottom2 * c 
            if top/(bottom1*bottom2) > 1000000:
                total = total + 1
    print(total)
    
comb()