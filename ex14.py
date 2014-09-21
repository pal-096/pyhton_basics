from sys import argv

first, second, other=argv

print "Hi %s, I'm the %s script. you must be the %s" %(second, first, other)
print "I'd like to ask you a few questions."

prompt = '-->'
print "Do you like me %s?" %second
likes = raw_input(prompt) 

print "where d you live %s?" % second
lives = raw_input(prompt)

print "what kind of computer you have?"
computer = raw_input(prompt)

print"""
Alright, so you said %s about liking me.
you live in %s. 
And you have a %s computer. nice.
"""%(likes, lives, computer)


