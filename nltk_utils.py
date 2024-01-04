import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def baf_of_words(tokenized_sentence, all_words):
    pass

a = "How long does shipping take?"
print(a)
a = tokenize(a)
print(a)