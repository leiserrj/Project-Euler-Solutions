def letters():
    total = 0
    
    values = {0: 0,1: 3,2: 3,3: 5,4: 4,5: 4,6: 3,7: 5,8: 5,9: 4,10: 4}
    ten = {0: 0,2: 6,3: 6,4: 5,5: 5,6: 5,7: 7,8: 6,9: 6}
    weird = {0: 3,1: 6,2: 6,3: 8,4: 8,5: 7,6: 7,7: 9,8: 8,9: 8}
    for x in range(1,1001,1):
        letters = 0
        hundreds = (x-x%100)/100
        tens = ((x-hundreds*100)-x%10)/10
        ones = x-(hundreds*100)-(tens*10)
        if x >= 100:
            letters = letters + values[hundreds] + 7
            if x%100 != 0:
                letters = letters + 3
        if x%100 >= 20:
            letters = letters + ten[tens]
        if tens == 1:
            letters = letters + weird[ones]
        else:
            letters = letters + values[ones]
        total = total + letters
    print(total)
    
letters()