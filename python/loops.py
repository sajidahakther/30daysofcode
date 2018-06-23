#001 - prints "Hello, I am an if statement and count is 0" once, 
# then "Hello, I am a while and count is 9" 9 times
count = 0

if count < 10:
  print "Hello, I am an if statement and count is", count

while count < 10:
  print "Hello, I am a while and count is", count
  count += 1
  
#002 - prints "i am a loop" once
loop_condition = True

while loop_condition:
  print "I am a loop"
  loop_condition = False
  
#003 - prints numbers from 1-10 squared
num = 1

while num < 11: 
  num_squared = num ** 2
  print num_squared
  num += 1

#004
choice = raw_input('Enjoying the course? (y/n)')

while choice != "y" and choice != "n": 
  choice = raw_input("Sorry, I didn't catch that. Enter again: ")

#005
count = 0

while count < 10: 
  print count
  count = count + 1
  
#006
count = 0

while True:
  print count
  count += 1
  if count >= 10:
    break
    
#007
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"
  
#008 Guess the number game
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3

while guesses_left != 0:
  guess = int(raw_input("Your guess: "))
  if (guess == random_number):
    print "You win!"
    break
  guesses_left = guesses_left - 1
else: 
  print "You lose."

#009
print "Counting..."

for i in range(20):
  print i
  
#010
hobbies = []

for num in range(3):
  hobby =  raw_input("Enter one of your hobbies: ")
  hobbies.append(hobby)

print hobbies

#011
thing = "spam!"
for c in thing:
  print c

word = "eggs!"
for i in word:
  print i
  
#012 - prints "X  b i r d  i n  t h e  h X n d . . ."
phrase = "A bird in the hand..."

for char in phrase:
  if char == "A" or char == "a":
    print "X", 
  else:
    print char,
    
print

#013 - print number squared
numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
  print num

for num in numbers:
  print num ** 2

#014 - prints 'a apple, b berry, c cherry'
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  print key, d[key]
  
#015 - prints 'Your choices are: 1 pizza, 2 pasta, 3 salad, 4 nachos' 
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index + 1, item
