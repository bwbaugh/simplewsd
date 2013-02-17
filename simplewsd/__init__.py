# Copyright (C) 2013 Brian Wesley Baugh
"""An English word sense disambiguation library using WordNet."""
import nltk


# TODO(bwbaugh): Only download resources after an error trying to use.
NLTK_DEPENDENCIES = [
                     'stopwords',
                    ]
downloader = nltk.downloader.Downloader()
for data in NLTK_DEPENDENCIES:
    if not downloader.is_installed(data):  # pragma: no branch
        downloader.download(data)  # pragma: no cover
