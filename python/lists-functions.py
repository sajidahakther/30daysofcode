#001 - prints 3
n = [1, 3, 5]
print n[1]

#002 - prints [1,15,5]
n = [1, 3, 5]
n[1]=n[1]*5
print n

#003 - prints [1,3,5,4]
n = [1, 3, 5]
n.append(4)
print n

#004 - prints [3,5]
n = [1, 3, 5]
n.pop(0)
print n

#005 - prints 15
number = 5
def my_function(x):
    return x * 3

print my_function(number)

#006 - prints 18
m = 5
n = 13
def add_function(x,y):
    return x+y

print add_function(m, n)

#007 - prints 'Helloworld'
n = "Hello"
def string_function(s):
    return s + "world"

print string_function(n)

#008 - prints [3,5,7]
def list_function(x):
    return x

n = [3, 5, 7]
print list_function(n)

#009-010 - prints [3,8,7]
def list_function(x):
    x[1] = x[1] + 3
    return x

n = [3, 5, 7]
print list_function(n)

#011 - prints [3,5,7,9]
n = [3, 5, 7]
def list_extender(lst):
    lst.append(9)
    return lst

print list_extender(n)

#012 - prints 3, 5, 7, None
n = [3, 5, 7]
def print_list(x):
    for i in range(0, len(x)):
        print x[i]

print print_list(n)

#013 - prints [0,1,2]
n = [3, 5, 7]
def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x

print double_list(n)

#014 - prints [0,1,2]
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print my_function(range(0,3))

#015 - prints 15
n = [3, 5, 7]
def total(numbers):
  result = 0
  for i in range(len(numbers)):
    result = result + numbers[i]
  return result

print total(n)

#016 - prints SajidahAkther
n = ["Sajidah", "Akther"]
# Add your function here
def join_strings(words):
  result = ""
  for i in words:
    result += i
  return result

print join_strings(n)

#017 - prints [1, 2, 3, 4, 5, 6]
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x, y):
  return x + y

print join_lists(m, n)

#018 - prints [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatten(lists):
  results = []
  for numbers in lists:
    results += numbers
  return results
   
print flatten(n)
