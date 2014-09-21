ten_things="Apples Oranges Crows Telephone Light Sugar"

print "Wait there are no 10 things in the list, lets fix that"

stuff = ten_things.split(' ')
more_stuff=["Day", "Dream", "good", "real", 
"ten", "four", "six", "vid"]

while len(stuff) !=10:
	next_one = more_stuff.pop()
	print "Adding:", next_one
	stuff.append(next_one)
	print "There are %d items now." %len(stuff)
	
print "There we go:", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ''.join(stuff)
print '#'.join(stuff[3:5])
