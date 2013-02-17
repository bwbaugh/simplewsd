# Copyright (C) 2013 Brian Wesley Baugh
from setuptools import setup, find_packages


program_name = 'simplewsd'
version = '0.1.0'


setup(
    name=program_name,
    version=version,
    packages=find_packages(),

    install_requires=open('requirements.txt').read(),

    author="B. W. Baugh",
    author_email="brian@brianbaugh.com",
    url="http://www.github.com/bwbaugh/" + program_name,
    description='An English word sense disambiguation library using WordNet.',
    long_description=open('README.md').read(),
    license='Creative Commons Attribution-NonCommercial-ShareAlike 3.0 '
            'Unported License',
    classifiers=[
                 "Intended Audience :: Developers",
                 "Intended Audience :: Science/Research",
                 "Natural Language :: English",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 2.6",
                 "Programming Language :: Python :: 2.7",
                 "Topic :: Scientific/Engineering :: Artificial Intelligence",
                 "Topic :: Scientific/Engineering :: Information Analysis",
                 "Topic :: Software Development :: Libraries :: Python Modules",
                 "opic :: Text Processing :: Linguistic",
                ],
)
