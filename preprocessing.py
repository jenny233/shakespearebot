'''
Preprocessing the poems.
Example usage:

import preprocessing as pp
X = pp.load_poems("data/shakespeare.txt")

'''

SYMBOL_LIST = {'?', '.',  ')', ',', '!', ';', '(', ':'}
def load_poems(filename):
    '''
    filename should be directory/filename
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
            # Add to the matrix of lines
            X.append(x)
    return X
