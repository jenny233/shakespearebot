'''
Trains the HMM model and generates poems
'''
import preprocessing as pp
import HMM
import random

word_list = pp.list_of_words()   # id   --> word
word_id = pp.word_id()           # word --> id
word_sylls = pp.word_syllables() # word --> n_syllables


poem_lines = pp.load_poems("shakespeare.txt")
rhyme_pairs = pp.rhyme_pairs(poem_lines)

# Train HMM
# hmm = HMM.unsupervised_HMM(poem_lines, 10, 100)
hmm = HMM.unsupervised_HMM(poem_lines, 1, 1)
print()


def generate_line(model, n_syllables, last_word):
    emission, states = model.generate_emission(n_syllables, last_word=last_word)
    line = ""
    for i in emission:
        line += word_list[i]
        line += " "
    return line.capitalize().strip()

def write_sonnet():
    # abab cdcd efef gg
    rhyming_tuples = []
    for i in range(7):
        rand_var = random.randrange(len(rhyme_pairs))
        rhyming_tuples.append(rhyme_pairs[rand_var])
    # rhyming_tuples[0][0], [1][0], [0][1], [1][1]
    #               [2][0], [3][0], [2][1], [3][1]
    #               [4][0], [5][0], [4][1], [5][1]
    #               [6][0], [6][1]
    i = 0
    while i <= 5:
        line = generate_line(hmm, 10, rhyming_tuples[i][0]) + ","
        print(line)
        line = generate_line(hmm, 10, rhyming_tuples[i+1][0]) + "."
        print(line)
        line = generate_line(hmm, 10, rhyming_tuples[i][1]) + ","
        print(line)
        line = generate_line(hmm, 10, rhyming_tuples[i+1][1]) + "."
        print(line)
        i += 2
    # Last couplet
    line = generate_line(hmm, 10, rhyming_tuples[i][0]) + ","
    print(line)
    line = generate_line(hmm, 10, rhyming_tuples[i][1]) + "."
    print(line)


write_sonnet()
# for i in range(14):
#     print(generate_line(hmm, 10, ""))
