from random import choice

from sys import argv


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_data = open(file_path).read()

    return file_data


def make_chains(text_string, n=3):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    word_list = text_string.split()

    for i in range(len(word_list)-n-1):
        try:
            idx = i
            n_gram = []
            while idx < i+n:
                n_gram.append(word_list[idx])
                idx += 1
            n_gram = tuple(n_gram)
        except KeyError:
            print "error"
        try:
            next_word = word_list[i+n] # "could"
        except IndexError:
            next_word = None
        if n_gram not in chains:
            chains[n_gram] = []
        chains[n_gram].append(next_word)

    print chains
    return chains

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    current_key = choice(chains.keys())
    text = " ".join(current_key)

    while True:

        try:
            next_random_word = choice(chains[current_key])

            text += " " + next_random_word

            current_key = (current_key[1], next_random_word)

        except TypeError:
            break

    return text


# Open the file and turn it into one long string
input_text = open_and_read_file(argv[1])

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
