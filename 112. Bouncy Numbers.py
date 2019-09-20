def increasing(num):
    for x in range(len(str(num))-1):
        if str(num)[x] > str(num)[x+1]:
            return False
    return True

def decreasing(num):
    for x in range(len(str(num))-1):
        if str(num)[x] < str(num)[x+1]:
            return False
    return True

def bouncy(num):
    if not increasing(num) and not decreasing(num):
        return True
    return False

num = 0
total = 0
correct = 0
while True:
    num += 1
    print(num)
    if bouncy(num):
        correct += 1
    total += 1
    if (correct*1.0) / total == .99:
        print(num)
        sys.exit(0)