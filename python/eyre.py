# There is a package called nltk. Loads it for this file.
import nltk

# Sets a variable filename for where our file is.
filename = "eyre.txt"

# Given a filename, opens it.
# "r" means read-only.
# "our_file" could be "chicken_nugget"
with open(filename, "r") as our_file:
    # Takes the file and reads the text. Stores it.
    text = our_file.read()

# Prints the first 100 characters, starting from 0 (so the first 99 characters).
print(text[0:100])

#Takes a long string and breaks it into words.
words = nltk.word_tokenize(text)
print(words[0:10])
