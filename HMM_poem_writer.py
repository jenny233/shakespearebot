'''
Trains the HMM model and generates poems
'''
import preprocessing as pp
import HMM

word_list = pp.list_of_words()
word_id = pp.word_id()

poem_lines = pp.load_poems("shakespeare.txt")
hmm = HMM.unsupervised_HMM(poem_lines, 4, 10)

# def generate_line(model, length)
#     emissions, states = model.generate_emission(length)
#     for id in emissions
#     for i in a[0]:
#         print(ivd[i])
