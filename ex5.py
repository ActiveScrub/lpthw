name = 'Alex Fernald'
age = 23 #factual
height = 67 * 2.54 #inches to centimeters
weight = 183 * 0.453592 #lbs
eyes = 'Brown'
teeth = 'Tan'
hair = 'Brown'

print("Let's talk about {}.".format(name))
print("He's {} centimeters tall.".format(height))
print("He's {} kilograms heavy.".format(weight))
print("Actually that's not too heavy.")
print("He's got {} eyes and {} hair.".format(eyes, hair))
print("His teeth are usually {} depending on the coffee.".format(teeth))

#Tricky line coming up
print("If I add {}, {}, and {} I get {}.".format(age, height, weight, age + height + weight))


