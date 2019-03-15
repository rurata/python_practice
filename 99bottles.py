num = 99
bots = ["bottles","bottle"]
ofbeer = ["of beer","on the wall"]
takeone= "Take one down, pass it around"
bot = bots[0]

while (num > 0):
	line1=[]
	line1.append(str(num))
	line1.append(bot)
	line1.append(" ".join(ofbeer))
	line2=[]
	line2.append(str(num))
	line2.append(bot)
	line2.append(ofbeer[0])
#	print line1
	
	print " ".join(line1)
	print " ".join(line2)
	print takeone
	num -= 1
	if (num != 1):
		bot = bots[0]
	else:
		bot = bots[1]
	line1[0] = str(num)
	line1[1] = bot
	print " ".join(line1)
	print "\n"