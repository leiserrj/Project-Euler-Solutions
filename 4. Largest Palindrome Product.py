def checkPal(num):
	numS = str(num)
	for x in range(len(numS)):
		if numS[x] != numS[len(numS)-x-1]:
			return False
		if x > len(numS)/2:
			return True
		
def Palindrome():
	max = 0
	for x in range(1000):
		for y in range(1000):
			if checkPal(x*y) == True and x*y > max:
				max = x*y
	print(max)
	
Palindrome()