def lex():
    perms = []
    for a in range(10):
        numbers = [a]
        for b in range(10):
            if b not in numbers:
                numbers.append(b)
                for c in range(10):
                    if c not in numbers:
                        numbers.append(c)
                        for d in range(10):
                            if d not in numbers:
                                numbers.append(d)
                                for e in range(10):
                                    if e not in numbers:
                                        numbers.append(e)
                                        for f in range(10):
                                            if f not in numbers:
                                                numbers.append(f)
                                                for g in range(10):
                                                    if g not in numbers:
                                                        numbers.append(g)
                                                        for h in range(10):
                                                            if h not in numbers:
                                                                numbers.append(h)
                                                                for i in range(10):
                                                                    if i not in numbers:
                                                                        numbers.append(i)
                                                                        for j in range(10):
                                                                            if j not in numbers:
                                                                                numbers.append(j)
                                                                                perms.append(int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)))
                                                                                print(numbers)
                                                                                del numbers[9]
                                                                        del numbers[8]
                                                                del numbers[7]
                                                        del numbers[6]
                                                del numbers[5]
                                        del numbers[4]
                                del numbers[3]
                        del numbers[2]
                del numbers[1]
        del numbers[0]
    print(sorted(perms)[999999])
    
lex()