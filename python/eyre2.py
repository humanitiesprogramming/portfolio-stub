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
print(words[0:30])

# print("words file type is",type(words)) # shows type is list

print(''' ''')
##########clear

clean_words =[] #create an empty list called clean_words
for word in words:  # step through the list, do this
        clean_words.append(word.lower()) # append, one at a time, the new, lowercased word for each
print(clean_words[0:30])

# print(f"clean_words is type",type(clean_words)) # verifies this is a list



# Counts the number of characters
#count_char:
#    text_length = len(text)
#    print(f"text length is {text_length}")
