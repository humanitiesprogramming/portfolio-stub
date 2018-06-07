# working with curled source text # refs a file already in the same directory
import nltk # there is a package called nltk. Load if for this file.

filename = "eyre.txt"

# given a filename open and read it, assign it to our_file, read and store it
with open(filename,'r') as our_file:
    text = our_file.read()
    # takes the file, reads it. stores it as a string

# print(text[0:100])
# print("text file type is",type(text)) # shows type is string

# take a long STRING and break it into words
words = nltk.word_tokenize(text)

print(words[0:1000])
# print("words file type is",type(words)) # shows type is list







# Counts the number of characters
#count_char:
#    text_length = len(text)
#    print(f"text length is {text_length}")
