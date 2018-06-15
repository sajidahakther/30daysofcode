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
