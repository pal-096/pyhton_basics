def add(a,b):
	print "Adding %d + %d" %(a,b)
	return a + b
	
def subtract(a,b):
	print "Subtracting %d-%d" %(a,b)
	return a - b
	
def multiply(a,b):
	print "Mutliplying %d*%d" %(a,b)
	return a * b

def divide(a,b):
	print "Dividing %d/%d" %(a,b)
	return a / b
	
print "Lets do some math with just functions!"

print "For adding age give the numbers"
age=add(int(raw_input()),int(raw_input()))
height=subtract(100, 20)
weight=multiply(200,10)
iq=divide(2000,3)

print "Age:%d, Height:%d, Weight:%d, IQ:%d" %(age,height,weight,iq)

print "Here is a small puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes:",what








