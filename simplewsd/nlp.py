# Copyright (C) 2013 Brian Wesley Baugh
"""Natural language processing (NLP) utility functions."""
import itertools
import re
import string
from nltk.corpus import stopwords as stopword_list


stopwords = stopword_list.words('english')


def no_stopwords(iterable, language='english'):
    """Generator that discards stopwords."""
    for x in iterable:
        if x not in stopwords:
            yield x


def no_punct(iterable):
    """Generator that discards punctuation-only tokens."""
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
