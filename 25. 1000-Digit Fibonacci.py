def digits():
    a = 1
    b = 1
    num = 2
    while len(str(b)) < 1000:
        temp = b
        b = a + b
        a = temp
        print(b)
        num = num + 1
    print(num)
    
digits()