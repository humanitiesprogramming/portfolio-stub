# working with curled source text # refs a file already in the same directory
import nltk                                 # there is a package called nltk. Load if for this file.

def open_file_and_get_text(filename):       # given a filename, openit
    with open(filename,'r') as our_file:
        text = our_file.read()
    return text              # takes the file, reads it. stores it as a string

def clean_tokens(words):
    clean_words =[] #create an empty list called clean_words
    for word in words:  # step through the list, do this
        clean_words.append(word.lower())
            # append, one at a time, the new, lowercased word for each
    return clean_words

###

our_file = "eyre.txt"

# this is an exmample of the pipeline
text = open_file_and_get_text(our_file)
words = nltk.word_tokenize(text)
print("These are words")
print(words[0:30])
clean_words = clean_tokens(words)
print("These are CLEAN WORDS")
print(clean_words[0:30])
word_counts = nltk.FreqDist(clean_words)
print("These are most_common words")
print(word_counts.most_common(10))
print("SHowing a given word and its count: Jane")
print(word_counts['jane']) # this works like the key, value in dictionary
nltk.Text(clean_words).dispersion_plot(['he','she','jane','tony'])
