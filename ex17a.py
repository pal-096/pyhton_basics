from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s." %(from_file,to_file)

in_file = open(from_file)
indata=in_file.read()

print "This input file is %d bytes." %len(indata)

print "Does, the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CNTRL-C to abort."
raw_input()

out_file=open(to_file, 'w')
out_file.write(indata)

print "done"

out_file.close()
in_file.close()
