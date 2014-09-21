from sys import argv
script, filename = argv

print "Im gng to close the file %r." %filename

print "Here we go"
raw_input("?")

print "opening the file--------"
target = open(filename,'w')

print "truncating the file.goodbye!"
target.truncate()

print "Now im gng to ask 3 lines"

one=raw_input("one:")
two=raw_input("two:")
three=raw_input("three:")
print "im gng to write this file."

target.write(one)
target.write("\n")
target.write(two)
target.write("\n")
target.write(three)
target.write("\n")
print "And we finally close it"
target.close()

