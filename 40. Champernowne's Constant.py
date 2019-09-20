def champ():
    total = 1
    num = ""
    for x in range(1,2000001):
        num = num + str(x)
    for y in range(7):
        total = total * int(num[10**y-1])
    print(total)

champ()