def lychrel():
    total = 0
    for x in range(1,10001):
        iterations = 0
        num = x
        while iterations <= 50:
            reverse = ''
            for y in range(len(str(num))-1,-1,-1):
                reverse = reverse + str(num)[y]
            num = num + int(reverse)
            
            for y in range(int(len(str(num)))):
                if str(num)[y] != str(num)[-y-1]:
                    break
            else:
                break
            iterations = iterations + 1
        if iterations >= 50:
            total = total + 1
    print(total)
    
lychrel()