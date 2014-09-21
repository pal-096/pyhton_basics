print "Let's practice everything"
print 'you\'d need to know \'bout escapes \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovely
and requires an explanation
\n\t\twhere there is none.
"""

print "@@@@@@@@@@@@@"
print poem
print "@@@@@@@@@@@@@"


five=10-2+4-6
print "This should be six:%s" %five

def secret_formula(started):
	jelly=started*500
	jars=jelly/1000
	crates=jars/100
	return jelly,jars,crates
	
start_point=10000
bar,cars,cranes = secret_formula(start_point)

print "With a starting point of:%d" % start_point
print "we'd have %d bar, %d cars, and %d cranes." %(bar,cars,cranes)

start_point=start_point/10

print "We can also do this way:"
print "We'd have %d bar, %d cars, and %d cranes." %secret_formula(start_point)

	
	
	






