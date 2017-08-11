import re #importing regular expressions library

#function which prompts user for dictionary name and handles FileNotFound exceptions

def file_load():
  while True:
    try:
      fname = input("Please enter the dictionary name: ")
      return open(fname)
    except FileNotFoundError:
      print("\n\n The file name you have entered cannot be found -_- \n\n")


def same(item, target):
  return len([item for (item, target) in zip(item, target) if item == target]) #returns number of letters and indexes in two words that match exactly

def build(pattern, words, seen, list):
  return [word for word in words #
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]

def find(word, words, seen, target, path):
  list = [] #creates an empty list
  for i in range(len(word)): #for loop which iterates through based on the length of the chosen word.
    list += build(word[:i] + "." + word[i + 1:], words, seen, list) #uses '.' as a wild card
  if len(list) == 0: #if the length of the list is 0 or empty
    return False
  list = sorted([(same(w, target), w) for w in list], reverse=True) #MAKE A LIST OF UNCOMMON CHARACTERS TO EXCLUDE DURING THE SEARCH AND COMPARE INDEXES TO EXLUDE FROM SEARCH!!! 3 - 4 LINES AT MAX#creates a list of nested tuples with the match value returned from the same function
  for (match, item) in list: #iterating through the match and word pairs in list
    if match >= len(target) - 1:
      if match == len(target) - 1: #is the final check to see if the next word is exactly the same as the target word. If it is then it appends that to the path and then breaks out of the function.
        path.append(item)
      return True #any return value will break out of the find function
    seen[item] = True #if the final word is not one change away then add it to the seen dictionary with a value of true
  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()





file = file_load()

lines = file.readlines()

while True:
  start = input("Enter start word:")
  target = input("Enter target word:")
  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
      words.append(word)

  break


count = 0
uncommon = ["x", "y", "z", "v"]
path = [start]
seen = {start : True}
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")


#HEY THESE VARIABLES ARE WRONG - TOMMI 2k17
#Read the PDF, Wayne is trying to syphon your soul.