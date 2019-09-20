def fifth():
    powers = []
    for x in range(10,500000):
        print(x)
        total = 0
        for y in range(len(str(x))):
            total = total + int(str(x)[y])**5
        if total == x:
            powers.append(x)
    print(sum(powers))
    
fifth()