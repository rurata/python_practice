
print "Please enter the triangle side lengths to check if a right triangle."
sides=[0,0,0]
for x in range(3):
	while True:
		try:
			num=str(x+1)
			side=raw_input("Side "+num+": ")
			s=float(side)
			break
		except ValueError:
			print "Enter a number!"
	sides[x]=s

sides.sort()

if (sides[2]**2==sides[0]**2+sides[1]**2):
	print "Yes! It is a right triangle!"
else:
	print "This isn't right!"