

# literal assignment
first = "Lutho"
last = "Sotsaka"

#print(type(first))
#print(type(first) == str)
#print(isinstance(first, str))

# constructor function
#pizza = str("Pepperoni")
#print(type(pizza))
#print(type(pizza) == str)
#print(isinstance(pizza, str))

#concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "S."
print(statement)

#Multiple lines
multinlines = '''
Hey, how are you?
I was just checking in.
                             Al good?

                             
'''
print(multinlines)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?/'
print(sentence)