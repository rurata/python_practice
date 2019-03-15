import math

grams = True
while True:
	lbs=raw_input("Please choose weight in (1) lbs or (2) grams: ")
	if (lbs=="1" or lbs=="2"):
		if (lbs=="1"):
			grams = False
			break
		else:
			grams = True
			break
	else:
		print "Please enter '1' or '2'"

#print "Please enter the total weight of each type of coin."
weights={"Pennies":2.5,"Nickels":5.0,"Dimes":2.268,"Quarters":5.67}
wrappers={"Pennies":50,"Nickels":40,"Dimes":50,"Quarters":40}
ncoin={"Pennies":0,"Nickels":0,"Dimes":0,"Quarters":0}
nwrap={"Pennies":0,"Nickels":0,"Dimes":0,"Quarters":0}
coinval={"Pennies":0.01,"Nickels":0.05,"Dimes":0.1,"Quarters":0.25}
total_value=0.

def roundup(fnum1,fnum2):
	num1=float(fnum1)
	num2=float(fnum2)
	mod = num1%num2
	if (num1/num2 > 1.):
		if (mod <= 1.e-10):
			return (num1/num2)
		else:
			return (math.floor(num1/num2) + 1.)
	else:
		return 1.

for key in weights:
	while True:
		try:
			tot=raw_input("Total weight of "+key+": ")
			w=float(tot)
			if (not grams):
				w=w*453.592
			break
		except ValueError:
			print "Please enter a valid number"
	ncoin[key]=int(roundup(w,weights[key]))
#	print ncoins,key
	nwrap[key]=int(roundup(ncoin[key],wrappers[key]))
#	print nwrap[key]

	print "You have: "+str(ncoin[key]),key
	print "You need: "+str(nwrap[key]),key,"wrappers"
	total_value=total_value+float(ncoin[key])*coinval[key]

print "You have approximately",total_value,"dollars"
