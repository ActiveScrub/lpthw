#Imports the argv function
from sys import argv

#Forces input from user to access file
script, filename = argv

#opens file
txt = open(filename)

#print called file without any parameters with intro line
print("Here's your file {}:".format(filename))
print(txt.read())

#prompts filename again to user
#print("Type the filename again:")
#file_again = input("> ")

##opens file
#txt_again = open(file_again)

##print called file without any parameters 
#print(txt_again.read())
