# There is a package called nltk. Loads it for this file.
import nltk

def open_file_and_get_text(filename):
    # Given a filename, opens it.
    # "r" means read-only.
    # "our_file" could be "chicken_nugget"
    with open(filename, "r") as our_file:
        # Takes the file and reads the text. Stores it.
        text = our_file.read()
    return text

# Given some tokens, lowercases them all.
def clean_tokens(words):
    # Creates an empty list called clean_words
    clean_words = []
    # Loops over each word item in the words list
    for word in words:
        # Makes each word item lowercase and appends it to the new list called clean_words
        clean_words.append(word.lower())
    return clean_words

# Sets a variable filename for where our file is.
filename = "eyre.txt"

text = open_file_and_get_text(filename)
#Takes a long string and breaks it into words.
words = nltk.word_tokenize(text)
clean_words = clean_tokens(words)
print(clean_words[0:30])
word_counts = nltk.FreqDist(clean_words)
print(word_counts.most_common(10))
print(word_counts["jane"])
nltk.Text(clean_words).dispersion_plot(["he", "she", "jane", "tony"])
