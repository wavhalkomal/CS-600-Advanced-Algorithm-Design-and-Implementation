"""
invertedindex.py
Author: Komal Wavhal (20034443)
Description: Mini Search Engine using Web Crawler and Inverted Index

Builds an inverted index from HTML pages and ranks query results using word frequency.
"""

import os
import re
from bs4 import BeautifulSoup

def load_stopwords(filepath="stopwords.txt"):
    """
    Loads stopwords (common words to ignore) from a file into a set.
    """
    with open(filepath, 'r') as f:
        return set(word.strip().lower() for word in f)

def tokenize(text, stopwords):
    """
    Preprocesses text: lowercase, remove punctuation, split into words, remove stopwords.
    """
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()
    return [word for word in words if word not in stopwords and word.isalpha()]

def build_index(folder, stopwords):
    """
    Reads HTML files from a folder and builds an inverted index.
    Format: {word: {filename: count}}
    """
    index = {}
    for filename in os.listdir(folder):
        if filename.endswith(".html"):
            filepath = os.path.join(folder, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
                text = soup.get_text()
                words = tokenize(text, stopwords)

                for word in words:
                    if word not in index:
                        index[word] = {}
                    if filename not in index[word]:
                        index[word][filename] = 0
                    index[word][filename] += 1

    return index