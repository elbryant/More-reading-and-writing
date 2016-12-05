#imports arguments
from sys import argv

#arguments used are script name and file name
script, filename = argv

#variable text is set to open the filename put in the arguments
txt = open(filename)

#it prints out the file name based on what was input
print "Here's your file %r:" % filename
#the system then reads the file
print txt.read()

#close opened file
txt.close()

#asks the user to type the file again
print "Type the filename again:"
#collects the raw input of what the user typed, adds a greater than before the prompt
file_again = raw_input("> ")

#opens the file again
txt_again = open(file_again)

#prints the file text
print txt_again.read()

#close open file
txt_again.close()