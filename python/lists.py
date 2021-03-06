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

#005 LIST SLICING
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle = suitcase[2:4]

# The last two items (index four and five)
last =  suitcase[4:6]
print middle
print suitcase

#006
animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:]

#007 INSERTING ANIMAL IN LIST
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]

duck_index = animals.index("duck")
animals.insert(duck_index, "cobra")

#inserted cobra at index 2, so duck shifts to index 3
print animals 

#008 MULTIPLYING INDICES IN LIST
my_list = [1,9,3,8,5,7]

for number in my_list:
  print 2 * number

#009 SQUARING AND SORTING LIST
start_list = [5, 3, 1, 2, 4]
square_list = []

for x in start_list:
    square_list.append(x**2)
square_list.sort()
print square_list

#010 ACCESSING VALUES BY KEYS
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] 
print residents['Sloth']
print residents['Burmese Python']

#011 ADDING KEY-VALUE PAIRS
menu = {} 
menu['Chicken Alfredo'] = 14.50 
print menu['Chicken Alfredo']

# Dish-price pairs to menu
menu['Pasta'] = 12.60
menu['Pizza'] = 17.00
menu['Lasagna'] = 13.20

print "There are " + str(len(menu)) + " items on the menu."
print menu

#012 DELETING ENTRIES AND OVERRIDDING VALUES
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}

del zoo_animals['Unicorn']
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

zoo_animals['Rockhopper Penguin'] = 'Rainforest Exhibit'

print zoo_animals

#013 REMOVING ITEMS
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')

#014 ADDING/SORTING/REMOVING - Key-value pairs
inventory = {
  'gold' : 500,
  # Assigning a list to 'pouch' and 'backpack' key
  'pouch' : ['flint', 'twine', 'gemstone'], 
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Adding a key 'pocket' and assigning a list to it
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# Sorting the list found under the key 'backpack'
inventory['backpack'].sort()

# Removing 'dagger' from backpack
inventory['backpack'].remove('dagger')

# Adding 50 to the number stored under the 'gold' key
inventory['gold'] = 550
