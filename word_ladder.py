import re #importing regular expressions library

#function which prompts user for dictionary name and handles FileNotFound exceptions then calls the file_load function, passing the file name into it as an argument.

def file_error_checker():
    while True:
        try:
            fname = input("Please enter the dictionary name: ")
            return file_load(fname)
        except FileNotFoundError:
            print("\n\n The file name you have entered cannot be found -_- \n\n")


#function which opens the file name passed to it by the file_error_checker() function above^

def file_load(file):
    return open(file, "r")


#function which prompts the user for a start word input and re-prompts until the input is satisfactory

def start_word_check(word):
    while True:
        if word.isdigit():
            word = input("\n\n\n Word cannot be a number. Please pick a start word\n\n\n>>>")
        elif len(word) < 2:
            word = input("\n\n\n Word must be at least 2 letters long. Please try another word\n\n\n>>>")
        elif word.isalpha():
            word.replace(" ", "")
            return word


#same as start word function except it also ensures that the target word word the user inputs is the same length as the start word.

def target_word_check(word):
    global start
    while True:
        if word.isdigit():
            word = input("\n\n\n Word cannot be a number. Please pick a target word\n\n\n>>>")
        elif len(word) != len(start):
            word = input("\n\n\n Word must be the same length as the start word you choose before. Please try another word\n\n\n>>>")
        elif word.isalpha():
            word.replace(" ", "")
            return word


#function which builds the list of the words which the user wishes to exclude from the search function and sanitizes the input to ensure the program will run correctly.

def forbidden_build(words):
    forbidden_words = words.split(',')
    return forbidden_words


#function which prompts the user for input which will determine whether they will be given the longest path or the shortest path. Input is sanitised to make sure it is not a number or

def path_selection(path):
    path.lower()
    while True:
        if (path.isdigit()):
            path = input("Input cannot be a number\n\n\n>>>").lower()
        elif len(path) >1:
            path = input("Please select either L or S\n\n\n>>>").lower()
        else:
            if path == 'l':
                return False
            elif path == 's':
                return True
            else:
                path = input("Please select either L or S\n\n\n>>>").lower()
                continue



#function which returns number of letters and indexes in two words that match exactly


def same(item, target):
  return len([item for (item, target) in zip(item, target) if item == target])


#function which iterates through all of the words in the words list and conducts a regular expression search on each word using a pattern and ensuring it is not already in the seen dictionary or in the path list.

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]


#function which:

#builds a list using the build function of all the possible variations of words in the dictionary.
#checks to see which path length the user has selected and adjusts the algorithm accordingly.
#selects the best possible word to then add to the path list based on the match value of a word returned from the same function.
#adds words to the seen dictionary to ensure word duplication will not occur.

def find(word, words, seen, target, path):
    global path_select
    global uncommon
    list = []
    for i in range(len(word)): #for loop which iterates through the word's letters based on the length of the chosen word.
        list += build(word[:i] + "." + word[i + 1:], words, seen, list) #uses '.' as a wild card
    if len(list) == 0:
        return False

    if path_select == True:
        list = sorted([(same(w, target), w) for w in list], reverse=True)
    else:
        uncommon = []
        list = sorted([(same(w, target), w) for w in list])
    for (match, item) in list: #iterating through the match and word pairs in list
        for letter in uncommon:
            if letter in item:
                list.remove((match, item))
        if match >= len(target) - 1:
            if match == len(target) - 1:
                path.append(item)
            return True
        seen[item] = True
    for (match, item) in list:
        path.append(item)
        if find(item, words, seen, target, path):
            return True
        path.pop()



#running all of the functions of the program


file = file_error_checker()

lines = file.readlines()

while True:

    #while loop which gathers all of the appropriate user input required for the program to run successfully.

    path = input("\n\n\nDo you want the shortest path or the longest path? Please input 'L' for the path or 'S' for the short path: \n\n >>>")
    path_select = path_selection(path.lower())
    word = input("Please enter start word:")
    start = start_word_check(word)
    word = input("Please enter target word:")
    target = target_word_check(word)
    words_list = str(input("\n\n\nPlease insert a list of words seperated by commas of words that you want to be excluded from the laddergram.\n\n\n\nHere is an example of how to format your input: \n\nhead, mead, dead \n\n\n>>>")).replace(" ", "")
    forbidden_words = forbidden_build(words_list)
    words = []
    for line in lines:
        word = line.rstrip()
        if len(word) == len(start) and word not in forbidden_words:
            words.append(word)

    break


count = 0
uncommon = ["x", "y", "z"]
path = [start]
seen = {start : True}

if find(start, words, seen, target, path):
    path.append(target)
    print(len(path) - 1, path)
else:
    print("No path found")

