from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_data = open(file_path).read()

    return file_data


def make_chains(text_string):
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

    for i in range(len(word_list)-1):
        bi_gram = (word_list[i], word_list[i+1]) # "("would", "you")
        try:
            next_word = word_list[i+2] # "could"
        except IndexError:
            next_word = None
        if bi_gram not in chains:
            chains[bi_gram] = []
        chains[bi_gram].append(next_word)
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    current_key = choice(chains.keys())

    while True:

        try:
            next_random_word = choice(chains[current_key])

            text += " ".join(current_key) + " " + next_random_word + " "

            current_key = (current_key[1], next_random_word)

        except TypeError:
            break

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
