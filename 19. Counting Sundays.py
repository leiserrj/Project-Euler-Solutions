def sundays():
    day = 1
    count = 0
    for x in range(1901,2002):
        if x%4 == 0 and x%400 != 0:
            for x in range(366):
                if x == 0 or x == 31 or x == 60 or x == 91 or x == 121 or x == 152 or x == 182 or x == 213 or x == 244 or x == 274 or x == 305 or x == 335:
                    if day == 0:
                        count = count + 1
                day = day + 1
                if day == 7:
                    day = 0
        else:
            for x in range(366):
                if x == 0 or x == 31 or x == 59 or x == 90 or x == 120 or x == 151 or x == 181 or x == 212 or x == 243 or x == 273 or x == 304 or x == 334:
                    if day == 0:
                        count = count + 1
                day = day + 1
                if day == 7:
                    day = 0
    print(count-1)
    
sundays()