def isCyclic(numList):
    for a in range(6):
        for b in range(6):
            if b == a:
                continue
            for c in range(6):
                if c == a or c == b:
                    continue
                for d in range(6):
                    if d == a or d == b or d == c:
                        continue
                    for e in range(6):
                        if e == a or e == b or e == c or e == d:
                            continue
                        f = 15 - a - b - c - d - e
                        positions = [a,b,c,d,e,f]
                        new = []
                        for x in positions:
                            new += [numList[x]]
                        if checker(new):
                            return True
    return False
                                       
def checker(numList):
    for x in range(len(numList)):
        if str(numList[x])[-2:] != str(numList[(x+1)%6])[:2]:
            return False
    return True

Triangle = 0
nTriangle = 1
while Triangle < 10000:
    Triangle = int((nTriangle * (nTriangle + 1)) / 2)
    nTriangle += 1
    if Triangle < 1000:
        continue
    Square = 0
    nSquare = 1
    while Square < 10000:
        Square = int(nSquare**2)
        nSquare += 1
        if Square < 1000:
            continue
        Pentagon = 0
        nPentagon = 1
        while Pentagon < 10000:
            Pentagon = int((nPentagon * (3 * nPentagon - 1)) / 2)
            nPentagon += 1
            if Pentagon < 1000:
                continue
            Hexagon = 0
            nHexagon = 1
            while Hexagon < 10000:
                Hexagon = int(nHexagon * (2 * nHexagon - 1))
                nHexagon += 1
                if Hexagon < 1000:
                    continue
                Heptagon = 0
                nHeptagon = 1
                while Heptagon < 10000:
                    Heptagon = int((nHeptagon * (5 * nHeptagon - 3)) / 2)
                    nHeptagon += 1
                    if Heptagon < 1000:
                        continue
                    Octagon = 0
                    nOctagon = 1
                    while Octagon < 10000:
                        Octagon = int(nOctagon * (3 * nOctagon - 2))
                        nOctagon += 1
                        if Octagon < 1000:
                            continue
                        if isCyclic([Triangle,Square,Pentagon,Hexagon,Heptagon,Octagon]):
                            print(sum([Triangle,Square,Pentagon,Hexagon,Heptagon,Octagon]))
                            sys.exit(0)
                        print([Triangle,Square,Pentagon,Hexagon,Heptagon,Octagon])
            
            