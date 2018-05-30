#001-002 PRINTING - Python 3/Python 2 syntax
print("Hello world!")
print "Hello world!"

#003-004 STRINGS - Combining Strings and Handing Errors ('/")
print "Hello " + "world!"
print 'Hello ' + 'world!'

#005 VARIABLES - Assigning Values
id = 123456

#006 ARITHMETIC OPERATIONS
product = 3*3
print(product)
remainder = (1398 % 11)
print(remainder)

#007 UPDATING VARIABLES
jan_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = jan_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

sept_to_dec_rainfall = 5.16 + 7.20 + 5.06 + 4.06
annual_rainfall += sept_to_dec_rainfall
print(annual_rainfall)

#008 COMMENTS
city_name = "St. Potatosburg"
#Population of St. Potatosburg is 340000
city_pop = 340000

#009 NUMBERS
cucumbers = 4
price_per_cucumber = 3.25
total_cost = (cucumbers * price_per_cucumber)
print(total_cost)

#010 TWO TYPES OF DIVISION
cucumbers = 100
num_people = 6

whole_cucumbers_per_person = (cucumbers / num_people)
print(whole_cucumbers_per_person)

cucumbers = 100.
num_people = 6.

float_cucumbers_per_person = (cucumbers / num_people)
print(float_cucumbers_per_person)

#011 MULTI-LINE STRINGS
haiku = """The old pond,
A frog jumps in:
Plop!"""

#012 BOOLEANS
age_is_21 = False
name_is_Sajidah = True

#013 VALUE ERROR - Converting Between Datatypes
float_1 = 0.25
float_2 = 40.0

product = float(float_1 * float_2)
big_string = ("The product was " + str(product))

print(big_string)

#014 REVIEW
skill_completed = "Python Syntax"
exercises_completed = 13

#The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5
point_total = 100
point_total += (exercises_completed*points_per_exercise)

print("I got " + str(point_total) + " points!")
