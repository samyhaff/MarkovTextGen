#!/usr/bin/env python

import re
import argparse
from collections import defaultdict
from random import choices

def process_text(raw_text):
    """Process a string to only return lowercase characters"""
    processed = re.sub(r'[^\w\s]', '', raw_text)
    processed = processed.lower()
    return processed

def create_chain(words, n_words=1):
    """creates the markov chain given a word list"""
    chain = defaultdict(lambda: defaultdict(lambda: 0))

    for i in range(len(words)-2*n_words+1):
        state = ' '.join(words[i:i+n_words])
        next_state = ' '.join(words[i+n_words:i+2*n_words])
        chain[state][next_state] += 1

    return chain

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
    chain = create_chain(words, n_words=2)
    print(chain['i do'])
