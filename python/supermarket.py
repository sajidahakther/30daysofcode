#001 FOR LOOP - Prints the names in the list
names = ["Adam","Alex","Mariah","Martine","Columbus"]

for i in ["Adam","Alex","Mariah","Martine","Columbus"]:
  print i

#002 LOOPING THROUGH WEBSTER DICTIONARY - Prints out definitions
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

for key in webster:
  print webster[key]

#003 EVEN NUMBERS
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in a:
  if i % 2 == 0:
    print i

#004 WORD OCCURRENCE
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count += 1
  return count

print fizz_count(["fizz", "cat", "fizz"])

#005 STRING LOOPING
for letter in "Codecademy":
  print letter

# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
  # Only print out the letter i
  if letter == "i":
    print letter

#006
prices = {
  "banana" : 4,
  "apple" : 2,
  "orange" : 1.5,
  "pear" : 3
}

#007-011 FRUIT PRICE, STOCK, TOTAL
prices = {
  "banana" : 4,
  "apple" : 2,
  "orange" : 1.5,
  "pear" : 3
}

stock = {
  "banana" : 6,
  "apple" : 0,
  "orange" : 32,
  "pear" : 15
}

# Price and stock of each fruit
for fruit in prices:
  print fruit
  print "- price: %s" % prices[fruit]
  print "- stock: %s" % stock[fruit]
  print

# Searching for the price and stock of a specific fruit
for fruit in prices:
  if fruit == "pear":
    print fruit
    print "* price: %s" % prices[fruit]
    print "* stock: %s" % stock[fruit]

# Total value of each/all fruit(s)
print
print "Total value of each fruit:"
total = 0
for fruit in prices:
  value = prices[fruit] * stock[fruit]
  print fruit + ": $" + str(value)
  total += value

print "Total value of all fruits: $" + str(total)
print

# Making a purchase, getting the price of a specific fruit
def compute_bill(fruit):
  total = 0
  for item in fruit:
    total = total + prices[item]
  return total

print "apple $" + str(compute_bill(["apple"]))
print "banana $" + str(compute_bill(["banana"]))

#012-013 STOCKING OUT
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total
