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

def load_poems(filename):
    '''
    filename should be directory/filename.
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

def rhyme_pairs(X):
    '''
    X is a matrix of words
    returns a list of tuples that rhyme
    '''
    rhyme_list = []
    lines_per_poem = [14] * 98
    lines_per_poem = lines_per_poem + [15]      # poem #99 has 15 lines
    lines_per_poem = lines_per_poem + [14] * 26
    lines_per_poem = lines_per_poem + [12]      # poem #126 has 12 lines
    lines_per_poem = lines_per_poem + [14] * 28
    
    line_number = 0
    for lpp in lines_per_poem:
        lines = X[line_number: line_number + lpp]
        line_number += lpp
        if lpp == 14:
            # poem follows abab cdcd efef gg
            # abab
            rhyme_list.append((lines[0][-1], lines[2][-1]))
            rhyme_list.append((lines[1][-1], lines[3][-1]))
            # cdcd
            rhyme_list.append((lines[4][-1], lines[6][-1]))
            rhyme_list.append((lines[5][-1], lines[7][-1]))
            # efef
            rhyme_list.append((lines[8][-1], lines[10][-1]))
            rhyme_list.append((lines[9][-1], lines[11][-1]))
            # gg
            rhyme_list.append((lines[12][-1], lines[13][-1]))
        elif lpp == 15:
            # poem follows abab h cdcd efef gg
            # abab
            rhyme_list.append((lines[0][-1], lines[2][-1]))
            rhyme_list.append((lines[1][-1], lines[3][-1]))
            # cdcd
            rhyme_list.append((lines[5][-1], lines[7][-1]))
            rhyme_list.append((lines[6][-1], lines[8][-1]))
            # efef
            rhyme_list.append((lines[9][-1], lines[11][-1]))
            rhyme_list.append((lines[10][-1], lines[12][-1]))
            # gg
            rhyme_list.append((lines[13][-1], lines[14][-1]))
        elif lpp == 12:
            # poem follows aabb ccdd eeff
            # aabb
            rhyme_list.append((lines[0][-1], lines[1][-1]))
            rhyme_list.append((lines[2][-1], lines[3][-1]))
            # ccdd
            rhyme_list.append((lines[4][-1], lines[5][-1]))
            rhyme_list.append((lines[6][-1], lines[7][-1]))
            # eeff
            rhyme_list.append((lines[8][-1], lines[9][-1]))
            rhyme_list.append((lines[10][-1], lines[11][-1]))
    return rhyme_list


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
