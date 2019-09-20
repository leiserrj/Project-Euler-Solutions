def pan():
    for x in range(9999,8999,-1):
        digits = []
        for y in range(4):
            if str(x)[y] not in digits and str(x)[y] != '0':
                digits.append(str(x)[y])
            else:
                break
        else:
            for z in range(5):
                if str(x*2)[z] in digits or str(x*2)[z] == '0':
                    break
                else:
                    digits.append(str(x*2)[z])
            else:
                print(str(x)+str(x*2))
                break
        
pan()