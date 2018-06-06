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
