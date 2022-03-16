#!/usr/bin/env python

import re
import argparse

def process_text(raw_text):
    """Process a string to only return lowercase characters"""
    processed = re.sub(r'[^\w\s]', '', raw_text)
    processed = processed.lower()
    return processed

def create_chain(words, n_words):
    """creates the markov chain given a word list"""
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='generate a nex text similar to the provided one')
    parser.add_argument('text', type=str, help='path to the input text')
    parser.add_argument('-w', '--words', type=int, default=1, help='number of words to use for a state')
    args = parser.parse_args()
    filename = args.text
    n_words = args.words

    with open(filename, encoding = "ISO-8859-1") as f:
        text = f.read().strip()

    words = process_text(text).split()
    print(words)
