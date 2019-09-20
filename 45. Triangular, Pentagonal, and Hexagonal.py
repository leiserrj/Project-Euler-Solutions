def thing():
    tri = []
    pent = []
    for x in range(1,287):
        tri.append((x*(x+1))/2)
        pent.append((x*(3*x-1))/2)
    while True:
        pos = len(tri)
        pos = pos + 1
        num = pos*(pos*2-1)
        tri.append(num)
        print(int(num))
        if num > pent[-1]:
            new = pent[-1]
            term = len(pent)
            while new < num:
                term = term + 1
                new = (term*(3*term-1))/2
                pent.append(new)
        if num in pent:
            print(num)
            break
        
thing()