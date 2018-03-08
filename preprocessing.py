'''
Preprocessing the poems.
Example usage:

import preprocessing as pp
X = pp.load_poems("data/shakespeare.txt")

'''

SYMBOL_LIST = {'?', '.',  ')', ',', '!', ';', '(', ':'}

word_list = []
word_sylls = {}
with open("data/Syllable_dictionary.txt") as f:
    while True:
        line = f.readline()
        if line == "":
            break
        line = line.strip()
        lst = line.split(" ", maxsplit=1)
        if len(lst) != 2:
            print(lst)
        word_list.append(lst[0])
        word_sylls[lst[0]] = lst[1].split(" ")

def load_poems(filename, onepoem=False):
    '''
    filename should be directory/filename.
    if onepoem, then only return data for the 1st poem.
    Returns the matrix X, where each row is a line of a poem, and each col is
            a word of the line.
    '''
    with open(filename) as f:
        # The matrix consisting of all lines
        X = []
        while True:
            line = f.readline()
            if line == "":
                break
            # Remove whitespaces from the front and back
            line = line.strip()

            if onepoem and line == "2":
                break

            # If it is not an actual poem line
            if len(line) < 5:
                continue
            # Remove punctuations
            for symbol in SYMBOL_LIST:
                line = line.replace(symbol, "")
            # Convert to lowercase
            line = line.lower()
            # Split into an array of words
            x = line.split(" ")
            # Check if it is in the Syllable_dictionary
            for i in range(len(x)):
                if not x[i] in word_list:
                    x[i] = x[i].replace("\'", "")
            # Add to the matrix of lines
            X.append(x)
    return X

def list_of_words():
    '''
    returns a list that maps id to word
    '''
    return word_list

def word_id():
    '''
    returns a dictionary that maps word to id
    '''
    dictionary = {}
    for i in range(len(word_list)):
        word = word_list[i]
        dictionary[word] = i
    return dictionary

def word_syllables():
    '''
    returns a dictionary that maps word to a list of potential number of
            syllables. Each element in the list is a string.
    '''
    return word_sylls
