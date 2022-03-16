# MarkovTextGen
Generate a text using markov chains

## Usage

```
usage: textgen.py [-h] [-w WORDS] [-l LENGTH] [-s START] text

generate a nex text similar to the provided one

positional arguments:
  text                  path to the input text

options:
  -h, --help            show this help message and exit
  -w WORDS, --words WORDS
                        number of words to use for a state
  -l LENGTH, --length LENGTH
                        length of the text to generate
  -s START, --start START
                        Starting text (must contain the specified number of words)
```
