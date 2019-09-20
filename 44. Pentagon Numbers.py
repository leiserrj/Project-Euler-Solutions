def pent():
    difference = 0
    pents = []
    for x in range(1,5000):
        pents.append(int((x*(3*x-1))/2))
    for a in pents:
        print(a)
        for b in pents:
            if a + b > pents[-1]:
                break
            if b > a:
                break
            if a - b in pents and a + b in pents and difference == 0:
                difference = a - b
            if a - b in pents and a + b in pents and a - b < difference:
                difference = a - b
    print(difference)            
pent()