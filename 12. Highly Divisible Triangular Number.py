def divisors(num):
    total = 1
    for x in range(1,int(num/2)+1,1):
        if num%x == 0:
            total = total + 1
    return total

def triangle():
    num = 1
    tri = 2
    while divisors(num) < 500:
        num = num + tri
        tri = tri + 1
    print(num)
    
triangle()