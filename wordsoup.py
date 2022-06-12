'''
this is a code for generating the kind of word-replacing "word soup"
introduced to me by lofty
the algorithm takes a text as input, and
replaces every nth word with the one n places later in the dictionary
as a dictionary, this program uses words.txt from https://github.com/dwyl/english-words
'''
from fuzzywuzzy import process

# set up the dictionary

dictionary = open('/usr/share/dict/words')
words_list = dictionary.readlines()
words_dict = {idx: el for idx, el in enumerate(words_list)}

def dict_get_word(word_in):
    '''
    gets the word 6 places along in the dictionary
    '''
    old_word = process.extract(word_in, words_dict)[0][2]
    return words_list[old_word + 6].strip()


def word_soup(text):
    '''
    transform given string;
    every 6th word is moved 6 places forward in the dictionary
    '''
    words = text.split()
    i = 0
    for word in words:
        if (i + 1) % 6 == 0:
            words[i] = dict_get_word(word)
        i += 1
    print(words)
