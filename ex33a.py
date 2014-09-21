numbers=[]
i=0

while i < 10:
	print "Top is %d" %i
	numbers.append(i)
	
	i=i+1
	
	print "The numbers now",numbers
	print "Now the bottom is %d" %i
	
for num in numbers:
	print num