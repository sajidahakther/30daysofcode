#001 LISTS
zoo_animals = ["pangolin", "cassowary", "sloth", "lion"];

if len(zoo_animals) > 3:
  print "The first animal at the zoo is the " + zoo_animals[0]
  print "The second animal at the zoo is the " + zoo_animals[1]
  print "The third animal at the zoo is the " + zoo_animals[2]
  print "The fourth animal at the zoo is the " + zoo_animals[3]
  
#002 ACCESS BY INDEX
numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
print numbers[1] + numbers[3]

#003 REPLACE/ASSIGN VALUES
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
zoo_animals[2] = "hyena"
zoo_animals[3] = "lion"

#004 LIST LENGTH
suitcase = [] 
suitcase.append("sunglasses")
suitcase.append("dress")
suitcase.append("bathing suit")
suitcase.append("sandals")

list_length = len(suitcase)

print "There are %d items in the suitcase." % (list_length)
print suitcase
