#001-003 BOOLEAN STATEMENTS - Assign True or False
# (20 - 10) > 15
bool_one = False
# (10 + 17) == 3**16 (** is 'to the power of')
bool_two = False
# 1**2 <= -1
bool_three = False
# 40 * 4 >= -4
bool_four = True
# 100 != 10**2
bool_five = False

#004-005 COMPARATORS
# Make me true!
bool_one = 3 < 5
# Make me false!
bool_two = 1 > 100
# Make me true!
bool_three = 62 >= 26
# Make me false!
bool_four = 5 != 5
# Make me true!
bool_five = 144 == 12*12

#006 AND
bool_one = False and False
bool_two = -(-(-(-2))) == -2 and 4 >= 16 ** 0.5
bool_three = -(-(-(-2))) == -2 and 4 >= 16 ** 0.5
bool_four = -(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2
bool_five = True and True

#007 OR
bool_one = 2 ** 3 == 108 % 100 or 'King James' == 'King Arthur'
bool_two = True or False
bool_three = 100 ** 0.5 >= 50 or False
bool_four = True or True
bool_five = 1 ** 100 == 100 ** 1 or 3 * 2 * 1 != 3 + 2 + 1

#008 NOT (false = true, true = false)
bool_one = not True
bool_two = not 3 ** 4 < 4 ** 3
bool_three = not 10 % 3 <= 10 % 2
bool_four = not 3 ** 2 + 4 ** 2 != 5 ** 2
bool_five = not not False

#009 NOT/AND/OR - What do the Booleans return?
# False or not True and True
bool_one = False
# False and not True or True
bool_two = True
# True and not (False or False)
bool_three = True
# not not True or False and not True
bool_four = True
# False or not (True and True)
bool_five = False

#010 COMPARATORS & BOOLEAN OPERATORS
# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!
# Make me true!
bool_two = 25 < 25 or "sajidah" != "akther"
# Make me false!
bool_three = not 40 > 0 and -1 < -100
# Make me true!
bool_four = "summer" == "productive" or 365 > 100
# Make me true!
bool_five = 10/2 == 5 and "sun" == "sun"

#011 CONDITIONAL STATEMENT SYNTAX
# Set response to 'Y' if you think the statement will print to the console
response = 'Y'
answer = "Left"
if answer == "Left":
    print "If nothing's going right, go left"

#012 IF STATEMENTS
def using_control_once():
    if 25 > 5:
        return "Success #1"

def using_control_again():
    if "sajidah" != "akther":
        return "Success #2"

print using_control_once()
print using_control_again()

#013 ELSE STATEMENTS
answer = "I am the black knight!"

def black_knight():
    if answer == "I am the black knight!":
        return True
    else:
        return False

def french_soldier():
    if answer == "I am a french soldier!":
        return True
    else:
        return False

#014 SWITCH-CASE STATEMENTS
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0

print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

#015 GRADE CONVERTER
# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80 and grade < 90:
        return "B"
    elif grade >= 70 and grade < 80:
        return "C"
    elif grade >= 65 and grade < 70:
        return "D"
    else:
        return "F"

# This prints an "A"
print grade_converter(92)
# This prints a "C"
print grade_converter(70)
# This prints an "F"
print grade_converter(61)
