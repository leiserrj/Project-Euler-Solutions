def fib():
    x = 0
    y = 1
    fib = 1
    sum = 0
    while fib < 4000000:
        fib = x + y 
        x = y
        y = fib
        if fib % 2 == 0:
            sum = sum + fib
    print(sum)
    
fib()