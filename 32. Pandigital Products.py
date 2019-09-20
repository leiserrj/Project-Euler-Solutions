def prod():
    total = 0
    answers = []
    for a in range(1,10000):
        digitsA = []
        for x in str(a):
            if x not in digitsA and x != '0':
                digitsA.append(x)
            else:
                break
        else:
            for b in range(1,a):
                digitsB = []
                if len(str(a)) + len(str(b)) + len(str(a*b)) > 9:
                    break
                if len(str(a)) + len(str(b)) + len(str(a*b)) < 9:
                    continue
                for x in str(b):
                    if x not in digitsA and x not in digitsB and x != '0':
                        digitsB.append(x)
                    else:
                        break
                else:
                    for x in str(a*b):
                        if x not in digitsA and x not in digitsB and x != '0':
                            digitsB.append(x)
                        else:
                            break
                    else:
                        if a*b not in answers:
                            total = total + (a*b)
                            answers.append(a*b)
                            print(a,b,a*b)
    print(total)
    
prod()