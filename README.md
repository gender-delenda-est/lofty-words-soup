# lofty-words-soup
A "word soup" generator algorithm

these functions use the fuzzywuzzy package to replace every 6th word in a piece of text with one 6 places further along in a dictionary

it is recommended that you install python-Levenshtein to support fuzzywuzzy

```
pip install fuzzywuzzy
pip install python-Levenshtein
```

# WARNING

1. this assumes you're on a linux computer with some kind of coherent file at ```/usr/share/dict/words``` if you don't have this, find your own dictionary and substitute it in the code.

2. this is absolutely slow as shit. do not run this on a long string if you value your CPU. i could probably optimise this but frankly i don't care enough

## usage

```python
>>> import wordsoup
>>> wordsoup.word_soup("some string to perform the conversion of")
```
