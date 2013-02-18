# Copyright (C) 2013 Brian Wesley Baugh
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install


program_name = 'simplewsd'
version = '0.1.0'
nltk_dependencies = [
                     'stopwords',
                    ]


class InstallWithPostCommand(install):
    def run(self):
        install.run(self)
        print 'running post install function'
        post_install()


def post_install():
    import nltk
    for resource in nltk_dependencies:
        if not nltk.download(resource):
            sys.stderr.write('ERROR: Could not download required NLTK resource:'
                             ' {}\n'.format(resource))
            sys.stderr.flush()


setup(
    name=program_name,
    version=version,
    packages=find_packages(),

    install_requires=open('requirements.txt').read(),
    cmdclass={'install': InstallWithPostCommand},

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
