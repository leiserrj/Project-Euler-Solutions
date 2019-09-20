def factSum():   
    total = 1
    for x in range(2,101,1):
        total = total*x 
    answer = 0
    for y in range(len(str(total))):
        answer = answer + int(str(total)[y])
    print(answer)
    
factSum()