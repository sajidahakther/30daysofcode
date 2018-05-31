#001-011 PYG-LATIN
pyg = 'ay'

original = raw_input('Enter a word:')
# checking if the word exists and if it contains letters
if len(original) > 0 and original.isalpha():
  print "your word: " + original
  word = original.lower()
  # gets the first index of the users word
  first = word[0]
  # 1: removes the first index from the whole word
  w = word[1:len(new_word)]
  # returns the word without the first index, then the first index, then 'ay'
  new_word = w + first + pyg
  print "translator: " + new_word
else:
  print "Empty"


 #EXPERIMENTING - Create a secret-key
varchar1 = 'lsg8q'
varchar2 = 'k3ny7h'
varchar3 = '2cb4'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print "Your word: " + original
  word = original.lower()
  first = word[0]
  fourth = "4v"
  w = word[1:len(new_word)]

  if len(original) >= 4:
    fourth = word[3]
    w = word[4:len(new_word)]

  new_word = fourth + varchar1 + w + varchar2 + first + varchar3
  print "Secret-key: " + new_word
else:
  print "Empty"
