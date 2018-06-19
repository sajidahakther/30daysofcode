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
