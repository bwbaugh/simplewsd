# Copyright (C) 2013 Brian Wesley Baugh
import string
from simplewsd.nlp import stopwords, no_stopwords, no_punct, split_on_punct


def test_no_stopwords():
    tokens = stopwords + ['happy']
    tokens = list(no_stopwords(tokens))
    assert tokens == ['happy']


def test_no_punct():
    tokens = ''.join(['a', string.punctuation, 'b'])
    tokens = ''.join(no_punct(tokens))
    assert tokens == 'ab'


def test_split_on_punct():
    assert not split_on_punct(string.punctuation)
