from sys import argv

script, filename, ben = argv

txt = open(filename)

print "here's your file %r:" %filename
print txt.read()
print "Name is %r:"%ben

print "Type the filename again:"
file_againagain = raw_input(">")

txt_again = open(file_againagain)

print txt_again.read()
