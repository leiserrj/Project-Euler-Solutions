def dist():
    num = 209
    while True:
        num = num + 1
        factors1 = []
        factor = 1
        temp = num
        while True:
            factor = factor + 1
            if factor > temp**.5 or temp == 1:
                factors1.append(factor)
                break
            if temp%factor == 0:
                temp = temp/factor
                if factor not in factors1:
                    factors1.append(factor)
                factor = factor - 1
        if len(factors1) != 4:
            continue
                
        factors2 = []
        factor = 1
        temp = num + 1
        while True:
            factor = factor + 1
            if factor > temp**.5 or temp == 1:
                factors2.append(factor)
                break
            if temp%factor == 0:
                temp = temp/factor
                if factor not in factors2:
                    factors2.append(factor)
                factor = factor - 1
        if len(factors2) != 4:
            continue
                
        factors3 = []
        factor = 1
        temp = num + 2
        while True:
            factor = factor + 1
            if factor > temp**.5 or temp == 1:
                factors3.append(factor)
                break
            if temp%factor == 0:
                temp = temp/factor
                if factor not in factors3:
                    factors3.append(factor)
                factor = factor - 1
        if len(factors3) != 4:
            continue
                
        factors4 = []
        factor = 1
        temp = num + 3
        while True:
            factor = factor + 1
            if factor > temp**.5 or temp == 1:
                factors4.append(factor)
                break
            if temp%factor == 0:
                temp = temp/factor
                if factor not in factors4:
                    factors4.append(factor)
                factor = factor - 1
        if len(factors4) == 4:
            print(num)
            break
        
dist()