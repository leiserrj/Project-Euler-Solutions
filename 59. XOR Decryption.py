def decrypt(key,message):
    dec = ''
    spot = 0
    for x in message:
        dec += chr(int(x)+key[spot])
        spot = (spot + 1) % 3
    return dec


file = open("XOR.txt","r")
for line in file:
    chars = line.strip().split(',')
for a in range(97,124):
    for b in range(97,124):
        for c in range(97,124):
            print([[a,b,c],decrypt([a,b,c],chars)])