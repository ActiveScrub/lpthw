#Variable equals string with format 
x = "There are {} types of people.".format("10")
#super redundant variable equals string
binary = "binary"
#another super redundant variable equals string
do_not = "don't"
#Variable as Excuse to use format insertion of last two redundant variables in a string
y = "Those who know {} and those who {}.".format(binary, do_not)

#Two Print Variables
print(x)
print(y)

print("I said: {}.".format(x))
print("I also said: '{}'.".format(y))

hilarious = False
joke_evaluation = "Isn't that joke so funny?!"

print(joke_evaluation, hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
