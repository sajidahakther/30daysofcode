#001 FUNCTIONS
def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print "With tax: %f" % bill
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print "With tip: %f" % bill
  return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

#002 FUNCTION JUNCTION
def spam():
  #docstring/optional comment explains what the function does
  """Prints 'Eggs!' to the console"""
  print "Eggs!"

# Define the spam function above this line.
spam()

#003 SQUARED
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)
  return squared

# Calling the square function, returns 10^2 which is 100
square(10)

#004 POWER
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)

#005 FUNCTIONS CALLING FUNCTIONS
def one_good_turn(n):
  return n + 1

def deserves_another(n):
  return one_good_turn(n) + 2

#006 CUBE
def cube(number):
  return number * number * number

def by_three(number):
  # checking if number is divisible by 3
  if number % 3 == 0:
    cube(number)
    return cube(number)
  else:
    return False

#007-008 IMPORTING Math Module
import math
# gets the square function from the maths module that's been imported
print math.sqrt(25)

#009-011 IMPORTING
# *just* the sqrt function from Math
from math import sqrt
# to import everything from maths
from math import *
#prints every function that's available within the maths Module
import math
everything = dir(math)
print everything

#012-015 MATH FUNCTIONS - Max/min/abs
def biggest_number(*args):
  print max(args)
  return max(args)

def smallest_number(*args):
  print min(args)
  return min(args)

def distance_from_zero(arg):
  print abs(arg)
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

#016 TYPE() - prints the type of data
print type(21)
print type(450000.00)
print type("morning")
# output: <type 'int'> <type 'float'> <type 'str'>

#017 SHUTDOWN
def shut_down(s):
  if s == "yes":
    return "Shutting down"

  elif s == "no":
    return "Shutdown aborted"

  elif s != "yes" and "no":
    return "Sorry"

#018-019
def distance_from_zero(n):
  if type(n) == int or type(n) == float:
    return abs(n)
  else:
    return "Nope"
