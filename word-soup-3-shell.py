# this is a code for generating the kind of word-replacing "word soup" introduced to me by lofty
# the algorithm takes a text as input, and replaces every nth word with the one n places later in the dictionary
# as a dictionary, this program uses words.txt from https://github.com/dwyl/english-words

from fuzzywuzzy import process

def dict_get_word(word_in):
    with open('words.txt') as words_file:
        words_list = words_file.readlines()
        words_dict = {idx: el for idx, el in enumerate(words_list)}
        old_word = process.extract(word_in, words_dict)[0][2]
        return words_list[old_word + 6].strip()


def word_soup(text):
    words = text.split()
    x = 0
    for word in words:
        if (x + 1) % 7 == 0:
            words[x] = dict_get_word(word)
        x += 1
    print(words)
