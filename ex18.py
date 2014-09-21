# this one is like your scripts with argv
def names (*args):
	arg1, arg2, arg3 = args
	print "arg1:%r, arg2:%r, arg3:%r" %(arg1, arg2, arg3)

	#ok, we can do this in another way also
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2:%r" %(arg1, arg2)
	
# this just takes one argument
def print_one(arg1):
	print "arg1:%r" % arg1
	
#this takes no arguments
def print_none():
	print "I got nothin'."
	
	
names("jack","four","tom")
print_two_again("jack","four")
print_one("First!")
print_none()
	
	