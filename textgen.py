#!/usr/bin/env python

import re
import argparse
from collections import defaultdict
from random import choices


def process_text(raw_text):
    """Process a string to only return lowercase characters"""
    processed = re.sub(r"[^\w\s]", "", raw_text)
    processed = processed.lower()
    return processed


def create_chain(words, n_words=1):
    """create the markov chain given a word list"""
    chain = defaultdict(lambda: defaultdict(lambda: 0))

    for i in range(len(words) - 2 * n_words + 1):
        state = " ".join(words[i : i + n_words])
        next_state = " ".join(words[i + n_words : i + 2 * n_words])
        chain[state][next_state] += 1

    return chain


def create_text(chain, start=None, length=10):
    """generate a new text given the markov chain"""
    if start is None:
        start = choices(list(chain.keys()))[0]
    elif start.lower() not in chain:
        raise Exception("Start string was not found in the given text")

    state = start.lower()
    new_text = state
    for _ in range(length):
        possibilities = list(chain[state].keys())
        if not possibilities:
            break
        weights = list(chain[state].values())
        state = choices(possibilities, weights=weights)[0]
        new_text += " " + state

    return new_text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="generate a nex text similar to the provided one"
    )
    parser.add_argument("text", type=str, help="path to the input text")
    parser.add_argument(
        "-w", "--words", type=int, default=1, help="number of words to use for a state"
    )
    parser.add_argument(
        "-l", "--length", type=int, default=20, help="length of the text to generate"
    )
    parser.add_argument(
        "-s",
        "--start",
        type=str,
        default=None,
        help="Starting text (must contain the specified number of words)",
    )

    args = parser.parse_args()
    filename = args.text
    n_words = args.words
    length = args.length
    start = args.start

    with open(filename, encoding="ISO-8859-1") as f:
        text = f.read().strip()

    # extract the words from the text file
    words = process_text(text).split()

    # generate the markov chain
    chain = create_chain(words, n_words=n_words)

    # generate the nesw text
    output = create_text(chain, start=start, length=length)
    print(output)
