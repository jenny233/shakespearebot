'''
Trains the HMM model and generates poems
'''
import preprocessing as pp
import HMM

word_list = pp.list_of_words()   # id   --> word
word_id = pp.word_id()           # word --> id
word_sylls = pp.word_syllables() # word --> n_syllables


poem_lines = pp.load_poems("shakespeare.txt")

# Train HMM
hmm = HMM.unsupervised_HMM(poem_lines, 10, 50)


def generate_line(model, n_syllables):

    emissions, states = model.generate_emission(n_syllables)
    line = ""
    for i in emissions:
        line += word_list[i]
        line += " "
    return line

# Write a sonnet
print()
for i in range(14):
    if i % 2 == 0:
        # even lines add comma (because it starts with 0)
        line = generate_line(hmm, 10).capitalize().strip() + ","
    else:
        # odd lines add period
        line = generate_line(hmm, 10).capitalize().strip() + "."
    print(line)
