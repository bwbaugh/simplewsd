# Copyright (C) 2013 Brian Wesley Baugh
import string
from nltk.corpus import stopwords
from simplewsd.nlp import word_tokenize, no_stopwords, no_punct, split_on_punct


def test_word_tokenize():
    # Text example from: http://nltk.org/api/nltk.tokenize.html
    sentence = 'Good muffins cost $3.88\nin New York.'
    tokens = ['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York', '.']
    result = word_tokenize(sentence)
    assert result == tokens


def test_no_stopwords():
    tokens = stopwords.words('english') + ['happy']
    tokens = list(no_stopwords(tokens))
    assert tokens == ['happy']


def test_no_punct():
    tokens = ''.join(['a', string.punctuation, 'b'])
    tokens = ''.join(no_punct(tokens))
    assert tokens == 'ab'


def test_split_on_punct():
    assert not split_on_punct(string.punctuation)
