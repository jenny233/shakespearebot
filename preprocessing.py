'''
Preprocessing the poems.
Example usage:

import preprocessing as pp
X = pp.load_poems("data/shakespeare.txt")

'''

SYMBOL_LIST = {'?', '.',  ')', ',', '!', ';', '(', ':'}

word_list = []
with open("data/Syllable_dictionary.txt") as f:
    while True:
        line = f.readline()
        if line == "":
            break
        line = line.strip()
        lst = line.split()
        word_list.append(lst[0])
print("word_list:", len(word_list))

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

def list_of_words(X):
    return word_list
