def dist():
    distincts = []
    for x in range(2,101,1):
        for y in range(2,101,1):
            if x**y not in distincts:
                distincts.append(x**y)
    print(len(distincts))
    
dist()