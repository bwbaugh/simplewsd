# Copyright (C) 2013 Brian Wesley Baugh
"""Natural language processing (NLP) utility functions."""
import itertools
import re
import string
import nltk
from nltk.corpus import stopwords


def word_tokenize(sentence):
    """Tokenize a single sentence."""
    return nltk.word_tokenize(sentence)


def no_stopwords(iterable):
    """Generator that discards stopwords."""
    for x in iterable:
        if x not in stopwords.words('english'):
            yield x


def no_punct(iterable):
    """Generator that discards stopwords."""
    for x in iterable:
        if x not in string.punctuation:
            yield x


def split_on_punct(text):
    """Split on any whitespace or punctuation."""
    pattern = r'[\s{0}]'.format(string.punctuation)
    tokens = list(no_punct(re.split(pattern, text)))
    assert not any(x == '' for x in tokens)
    assert not any(x in string.punctuation for x in itertools.chain(tokens)), tokens
    return tokens
