def fract():
    nums = []
    for x in range(10,100):
        for y in range(x+1,100):
            if str(x)[1] != '0' and str(y)[1] != '0' and str(x)[0] != str(x)[1]:
                if x/y == int(str(x)[0])/int(str(y)[0]) and str(x)[1] == str(y)[1] or x/y == int(str(x)[0])/int(str(y)[1]) and str(x)[1] == str(y)[0] or x/y == int(str(x)[1])/int(str(y)[0]) and str(x)[0] == str(y)[1] or x/y == int(str(x)[1])/int(str(y)[1]) and str(x)[0] == str(y)[0]:
                    nums.append(x)
                    nums.append(y)
    print(nums[0]*nums[2]*nums[4]*nums[6]/(nums[1]*nums[3]*nums[5]*nums[7]))

fract()