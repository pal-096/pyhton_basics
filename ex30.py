people = 30
cars = 40
trucks = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We cant decide"

trucks += 25

if trucks < cars:
	print "Thats too many trucks"
elif trucks > cars:
	print "maybe we could take the trucks"
else:
	print "We cant decide"
	
if people < trucks:
	print "Alright, lets just take the trucks"
else:
	print "Fine, lets stay home then"
	
