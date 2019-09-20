def digits(num):
    digitList = []
    for x in str(num):
        digitList += [x]
    return sorted(digitList)

num = 100
while True:
    num += 1
    if len(str(num)) != len(str(6*num)):
        continue
    list1 = digits(num)
    list2 = digits(2*num)
    list3 = digits(3*num)
    list4 = digits(4*num)
    list5 = digits(5*num)
    list6 = digits(6*num)
    for x in list1:
        if x in list2 and x in list3 and x in list4 and x in list5 and x in list6:
            list2.remove(x)
            list3.remove(x)
            list4.remove(x)
            list5.remove(x)
            list6.remove(x)
        else:
            break
    else:
        print(num)
        break