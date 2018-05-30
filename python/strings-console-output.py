#001-002 STRINGS AND CONSOLE OUTPUT
caesar = "Graham"
praline = "John"
viking = "Teresa"

print caesar
print praline
print viking

#003 ESCAPING CHARACTERS - Adding backslash to stop apostrophe ending String
'This isn\'t flying, this is falling with style!'

#004 ACCESS BY INDEX - Prints Y
fifth_letter = "MONTY"[4]
print fifth_letter

#005-009 METHODS & DOT NOTATION

#dot notation only work with Strings; methods make text lowercase/uppercase
parrot = "Norwegian Blue"
print parrot.lower()
print parrot.upper()

#methods work on other data types; str() turns non-strings into strings, len() gets length of string - prints 7.
student = "Sajidah"
year = 2018
print student + " was born in " + str(year)
print len(student)

#010-013 PRINTING STRING CONCATENATION
print "Spam " + "and " + "eggs"

#014 STRING FORMATTING WITH %
string_1 = "waffles"
string_2 = "ice-cream"
print "I am hungry. I am craving %s and %s." % (string_1, string_2)

#015 CONSOLE INPUT/OUTPUT & % FORMATTING
name = raw_input("What is your name? ")
interest = raw_input("What are you interested in? ")
colour = raw_input("What is your favorite colour? ")

print " "
print("Ah, so your name is " + name + ", you are interested in " + interest + ". Your favourite colour is " + colour + ".")
print " "

name = "Sajidah"
interest = "coding"
colour = "black"

print "My name is %s, I am interested in %s. My favourite colour is %s." % (name, interest, colour)

#016
my_string = "I have reached the end"
print len(my_string)
print my_string.upper()
